import system
system.path.append('..')
import random
from datetime import datetime, timedelta
from typing import List

from overrides import overrides
import jpbizday

from algotham.rule import (
    BaseStockSelectionRule,
    BaseTimingRule,
    BaseVolumeRule
)
from algotham.data.stock import Stock
from algotham.algo_runner import SimulatedAlgoSystem


# 毎日マーケットオープン時に候補銘柄からランダムに銘柄抽出し、ランダムなボリュームで売買行う例


class RandomStockSelectionRule(BaseStockSelectionRule):

    STOCK_CANDIDATES = [3853, 3987, 6029, 4120, 3747]

    @overrides
    def select_stocks(self) -> List[Stock]:

        selected_codes = random.sample(
            RandomStockSelectionRule.STOCK_CANDIDATES,
            3
        )
        stocks = [Stock(code=code) for code in selected_codes]
        return stocks


start_dt = 


class MarketOpeningTimingRule(BaseTimingRule):

    def __init__(self):
        self._next_opening = start_dt
        self._next_opening.hour = 9
        self._next_opening.minute = 0
        self._next_opening.second = 0

    @overrides
    def wait_for_next(self):
        self._next_opening += timedelta(days=1)
        while not jpbizday.is_bizday(self._next_opening):
            self._next_opening += timedelta(days=1)
            print(f'waing until {self._next_opening }')
        self.wait_until(self._next_opening)


class RandomVolumeRule(BaseVolumeRule):

    @overrides
    def decice_volume(self, stock: Stock, dt: datetime) -> int:
        return random.randint(-5, 5)


random_trade_system = SimulatedAlgoSystem(
    timing_rule=MarketOpeningTimingRule(),
    stock_selection_rule=RandomStockSelectionRule(),
    volume_rule=RandomVolumeRule(),
)

back_test = BackTest(
    random_trade_system,
    start_dt=,
    end_dt=,
)
backtest.run()
result = backtest.result()
