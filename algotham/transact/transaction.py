from abc import ABCMeta, abstractmethod
from datetime import datetime

from overrides import overrides

from ..data.stock import Stock
from ..utils.logger import Logger


class BaseTransaction(metaclass=ABCMeta):

    TAG = 'BaseTransaction'

    def __init(self):
        self._algo = None

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

        if self._algo._portfolio.transact(stock, volume):
            self._algo.recorder.record(dt, stock, volume)
        else:
            Logger.i(
                BaseTransaction.TAG,
                f'Skipped transaction, stock : {stock.code}, volume : {volume}'
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
