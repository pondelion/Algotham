from abc import ABCMeta, abstractmethod
import os

import pandas as pd

from ..storage import S3
from ..utils.logger import Logger


class CSVHistoricalData(metaclass=ABCMeta):

    TAG = 'CSVHistoricalData'
    _cache = {}

    @property
    def historical(self) -> pd.DataFrame:
        return self._historical()

    def _historical(self):

        local_cache_path = self._local_cache_path()

        if local_cache_path in CSVHistoricalData._cache:
            return CSVHistoricalData._cache[local_cache_path]

        # If cache file already exists, use it.
        if os.path.exists(local_cache_path):
            CSVHistoricalData._cache[local_cache_path] = pd.read_csv(local_cache_path)
            return CSVHistoricalData._cache[local_cache_path]

        # Download csv file from S3.
        source_path = self._source_path()
        self._download_s3_file(
            local_cache_path,
            source_path,
        )
        CSVHistoricalData._cache[local_cache_path] = pd.read_csv(local_cache_path)
        return CSVHistoricalData._cache[local_cache_path]

    @abstractmethod
    def _local_cache_path(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _source_path(self) -> str:
        raise NotImplementedError

    def _download_s3_file(
        self,
        local_dest_path: str,
        source_path: str
    ) -> None:
        os.makedirs(os.path.dirname(local_dest_path), exist_ok=True)
        Logger.i(CSVHistoricalData.TAG, f'Downloading {source_path} to {local_dest_path}')
        S3.download_file(source_path, local_dest_path)
