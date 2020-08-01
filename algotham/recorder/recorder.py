from copy import copy
from datetime import datetime
from typing import Dict

from ..portfolio import Portfolio
from ..data.stock import Stock


class Recorder:

    def __init__(
        self,
        cash: int = 0,
        dt: datetime = datetime.now(),
        stocks: Dict[int, int] = {},
    ):
        self._cash = cash
        self._cash_history = [
            (dt, cash)
        ]
        self._stocks = copy(stocks)
        self._stock_history = [
            (dt, copy(stocks))
        ]
        self._transaction_history = []

    def record_portfolio(
        self,
        dt: datetime,
        portfolio: Portfolio
    ) -> None:
        pass

    def record_transaction(
        self,
        dt,
        stock: Stock,
        volume: int,
    ) -> None:
        pass
