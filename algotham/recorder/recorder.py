from copy import copy
from datetime import datetime
from typing import Dict


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

    def record(self, portfolio):
        raise NotImplementedError
