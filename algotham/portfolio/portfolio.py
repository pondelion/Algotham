from typing import Dict
from datetime import datetime
from copy import copy

from ..data.stock import (
    Stock,
    StockDataNotFoundException
)


class Portfolio:

    def __init__(
        self,
        cash: int = 0,
        stock_volume: Dict[int, int] = {}
    ):
        self._cash = cash
        self._stock_volume = copy(stock_volume)

    def update(
        self,
        cash: int,
        stock: Stock,
        volume: int,
    ) -> None:
        self._cash += cash
        if stock.code in self._stock_volume:
            self._stock_volume[stock.code] += volume
        else:
            self._stock_volume[stock.code] = volume
