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
        cash_diff: int,
        stock: Stock,
        volume_diff: int,
    ) -> None:
        self._cash += cash_diff
        if stock.code in self._stock_volume:
            self._stock_volume[stock.code] += volume_diff
        else:
            self._stock_volume[stock.code] = volume_diff

    @property
    def cash(self):
        return self._cash

    @property
    def stock_volume(self):
        return self._stock_volume

    def evaluate_total_asset(self, dt: datetime) -> int:
        cash = self._cash

        for code, volume in self._stock_volume.items():
            try:
                stock_price = Stock(code=code)[dt]
                cash += stock_price * volume
            except Exception:
                raise StockDataNotFoundException(
                    f'code = {code}, datetime = {dt}'
                )

        return cash
