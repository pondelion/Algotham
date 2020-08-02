import sys
sys.path.append('..')
import random
from datetime import datetime, timedelta
from typing import List

from overrides import overrides
import jpbizday
import pandas as pd

from algotham.rule import (
    BaseStockSelectionRule,
    BaseTimingRule,
    BaseVolumeRule
)
from algotham.data.stock import Stock
from algotham.algo import SimulatedAlgo
from algotham.simulator.backtest import BackTest
from algotham.portfolio import Portfolio


# ボリンジャーバンド1σ線を越えたら売買を行う例


def create_signal(stock):
    df = stock.historical.copy()
    df['日付'] = pd.to_datetime(df['日付'])
    df.set_index('日付', inplace=True)
    df['rolling15_lower_sigma'] = df['始値'].rolling(window=15).mean() - df['始値'].rolling(window=15).std()
    df['rolling15_upper_sigma'] = df['始値'].rolling(window=15).mean() + df['始値'].rolling(window=15).std()
    df.dropna(inplace=True)
    df['price_over_lower_sigma'] = df['始値'] > df['rolling15_lower_sigma']
    df['price_over_upper_sigma'] = df['始値'] > df['rolling15_upper_sigma']
    df['buy_signal'] = (df['price_over_lower_sigma'] == False) & (df['price_over_lower_sigma'].shift(1) == True)
    df['sell_signal'] = (df['price_over_upper_sigma'] == True) & (df['price_over_upper_sigma'].shift(1) == False)
    return df


class StockSelectionRule(BaseStockSelectionRule):

    STOCKS = [3853, 3987, 6029, 4120, 3747]

    @overrides
    def select_stocks(self, dt: datetime) -> List[Stock]:
        stocks = [Stock(code=code) for code in StockSelectionRule.STOCKS]
        return stocks


signals = {code: create_signal(Stock(code=code)) for code in StockSelectionRule.STOCKS}

start_dt = datetime(2019, 4, 1)
end_dt = datetime(2019, 7, 1)


class EverydayTimingRule(BaseTimingRule):

    def __init__(self):
        self._next_day = start_dt
        self._next_day = self._next_day.replace(
            hour=10,
            minute=0,
            second=0
        )

    @overrides
    def wait_for_next(self):
        self._next_day += timedelta(days=1)
        while not jpbizday.is_bizday(self._next_day):
            self._next_day += timedelta(days=1)
        print(f'waiting until {self._next_day }')
        self.wait_until(self._next_day)


class BollingerBandVolumeRule(BaseVolumeRule):

    @overrides
    def decide_volume(self, stock: Stock, dt: datetime) -> int:
        dt_idx = datetime(dt.year, dt.month, dt.day)
        try:
            buy_sig = signals[stock.code].loc[dt_idx, 'buy_signal']
            sell_sig = signals[stock.code].loc[dt_idx, 'sell_signal']
        except Exception as e:
            print(f'Skipping transaction : {e}')
            return 0

        if buy_sig and sell_sig:
            print('Something wrong')
            return 0
        rand_volume = random.randint(1, 5)
        if buy_sig:
            return rand_volume
        elif sell_sig:
            return -rand_volume
        else:
            return 0


bollinger_trade_algo = SimulatedAlgo(
    timing_rule=EverydayTimingRule(),
    stock_selection_rule=StockSelectionRule(),
    volume_rule=BollingerBandVolumeRule(),
    init_portfolio=Portfolio(cash=100000)
)

back_test = BackTest(bollinger_trade_algo)
back_test.run(
    start_dt=start_dt,
    end_dt=end_dt,
)
result = back_test.result()
print('done')

print(result.transaction_history)
portfolio_history = result.portfolio_history
df_portfolio_history = pd.DataFrame({
    'datetime': portfolio_history['datetime'],
    'total_asset': portfolio_history['total_asset']
})
df_portfolio_history['datetime'] = pd.to_datetime(df_portfolio_history['datetime'])
print(df_portfolio_history)
