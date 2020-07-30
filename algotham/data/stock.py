import os

from overrides import overrides

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
        if code is None and company_name is not None:
            self._code = company_name2code(company_name)

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
