from copy import copy
from datetime import datetime
from typing import Dict

import pandas as pd

from ..portfolio import Portfolio
from ..data.stock import (
    Stock,
    StockDataNotFoundException
)


class Recorder:

    def __init__(self):
        self.reset()

    def record_portfolio(
        self,
        dt: datetime,
        portfolio: Portfolio
    ) -> None:
        self._portfolio_history['datetime'].append(dt)
        self._portfolio_history['stock_volume'].append(copy(portfolio.stock_volume))
        try:
            total_asset = portfolio.evaluate_total_asset(dt)
        except StockDataNotFoundException:
            total_asset = None
        self._portfolio_history['total_asset'].append(total_asset)

    def record_transaction(
        self,
        dt,
        stock: Stock,
        volume: int,
    ) -> None:
        self._transaction_history['datetime'].append(dt)
        self._transaction_history['stock'].append(stock.code)
        self._transaction_history['volume'].append(volume)

    def reset(self):
        self._portfolio_history = {
            'datetime': [],
            'stock_volume': [],
            'total_asset': [],
        }
        self._transaction_history = {
            'datetime': [],
            'stock': [],
            'volume': []
        }

    @property
    def transaction_history(self):
        df = pd.DataFrame(self._transaction_history)
        df['datetime'] = pd.to_datetime(df['datetime'])
        return df

    @property
    def portfolio_history(self):
        return self._portfolio_history
