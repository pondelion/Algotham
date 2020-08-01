import os
from datetime import datetime, date

from overrides import overrides
import pandas as pd

from .historical_data import CSVHistoricalData
from ..utils.config import DataLocationConfig


class Stock(CSVHistoricalData):

    def __init__(
        self,
        code: int = None,
        company_name: str = None,
    ):
        self._code = code
        self._company_name = company_name
        # if code is None and company_name is not None:
        #     self._code = company_name2code(company_name)

    @property
    def code(self) -> int:
        return self._code

    @property
    def company_name(self) -> str:
        return self._company_name

    @overrides
    def _local_cache_path(self) -> str:
        local_cache_path = os.path.join(
            DataLocationConfig.LOCAL_CACHE_DIR,
            'stock',
            f'{self._code}.csv'
        )
        return local_cache_path

    @overrides
    def _source_path(self) -> str:
        source_path = os.path.join(
            DataLocationConfig.STOCKPRICE_CONCAT_BASEDIR,
            f'{self._code}.csv'
        )
        return source_path

    def __getitem__(self, dt):
        if not isinstance(dt, datetime):
            raise Exception('Only datetime type index accessing is supported.')

        df = self._historical()
        #print(df)
        if '日付' in df.columns:
            df['日付'] = pd.to_datetime(df['日付'])
            df.set_index('日付', inplace=True)
        #print(df)
        print(self.code)
        try:
            dt_idx = datetime(dt.year, dt.month, dt.day)
            stock_price = df.loc[dt_idx, '始値']
            stock_price += df.loc[dt_idx, '終値']
        except Exception:
            raise StockDataNotFoundException(f'stock data not found : {dt_idx}')
        return stock_price // 2

    # @staticmethod
    # def data(code: int):
    #     local_cache_path = os.path.join(
    #         DataLocationConfig.LOCAL_CACHE_DIR,
    #         'stock',
    #         f'{code}.csv'
    #     )
    #     if local_cache_path in Stock._cache:
    #         return Stock._cache[local_cache_path]


class StockDataNotFoundException(Exception):
    pass
