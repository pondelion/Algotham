from abc import ABCMeta, abstractmethod
from datetime import datetime

from overrides import overrides

from ..data.stock import (
    Stock,
    StockDataNotFoundException
)
from ..utils.logger import Logger


class BaseTransaction(metaclass=ABCMeta):

    TAG = 'BaseTransaction'

    def __init__(self, transaction_cost: int = 0):
        self._algo = None
        self._transaction_cost = transaction_cost

    def set_context(
        self,
        algo
    ) -> None:
        self._algo = algo

    @property
    def context(self):
        return self._algo

    @abstractmethod
    def on_transact(
        self,
        dt: datetime,
        stock: Stock,
        volume: int
    ) -> None:
        raise NotImplementedError

    def transact(
        self,
        dt: datetime,
        stock: Stock,
        volume: int
    ) -> None:
        self._default_transact(dt, stock, volume)
        self.on_transact(dt, stock, volume)

    def _default_transact(self, dt, stock, volume):
        if self._algo is None:
            raise Exception('context is not set')

        skip_reason = ''

        while True:
            if volume == 0:
                skip_reason = 'volume is 0'
                break

            try:
                price = stock[dt] * volume
            except StockDataNotFoundException as e:
                print(e)
                skip_reason = 'stock price data is missing'
                break

            # If the cash is insufficient to buy stock, skip buying.
            if volume >= 0 and price + self._transaction_cost > self._algo.portfolio._cash:
                skip_reason = 'cash is insufficient to buy stock'
                break

            # If the stock is insufficient to sell, skip selling.
            if volume < 0 and stock.code not in self._algo.portfolio._stock_volume:
                skip_reason = 'stock is insufficient to sell'
                break
            elif volume < 0 and self._algo.portfolio._stock_volume[stock.code] < abs(volume):
                skip_reason = 'stock is insufficient to sell'
                break

            cash = -(price + self._transaction_cost)

            print(f'buy/sell : code={stock.code} : volume={volume} : cash={cash} : ')
            self._algo._portfolio.update(cash, stock, volume)
            self._algo.recorder.record_transaction(dt, stock, volume)
            self._algo.recorder.record_portfolio(dt, self._algo.portfolio)
            return

        Logger.i(
            BaseTransaction.TAG,
            f'Skipped transaction, stock={stock.code}, volume={volume} : {skip_reason}'
        )


class DefaultTransaction(BaseTransaction):

    @overrides
    def on_transact(
        self,
        dt: datetime,
        stock: Stock,
        volume: int
    ) -> None:
        pass
