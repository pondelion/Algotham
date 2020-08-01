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

    def transact(
        self,
        dt: datetime,
        stock: Stock,
        volume: int,
        transaction_cost: int,
    ) -> bool:

        if volume == 0:
            return False

        try:
            price = stock[dt] * volume
        except StockDataNotFoundException as e:
            print(e)
            return False

        # If the cash is insufficient to buy stock, skip buying.
        if volume >= 0 and price + transaction_cost > self._cash:
            return False

        # If the stock is insufficient to sell, skip selling.
        if volume < 0 and stock.code not in self._stock_volume:
            return False
        elif volume < 0 and self._stock_volume[stock.code] < abs(volume):
            return False

        print('buy/sell')
        self._cash -= price + transaction_cost
        if stock.code in self._stock_volume:
            self._stock_volume[stock.code] += volume
        else:
            self._stock_volume[stock.code] = volume

        return True
