from abc import ABCMeta, abstractmethod
import os

import pandas as pd


class CSVHistoricalData(metaclass=ABCMeta):

    def __init__(self):
        self._historical_data = None

    @property
    def historical(self) -> pd.DataFrame:
        return self._histrical()

    def _historical(self):
        if self._historical_data is not None:
            return self._historical_data

        local_cache_path = self._local_cache_path()
        # If cache file already exists, use it.
        if os.path.exists(local_cache_path):
            self._historical = pd.read_csv(local_cache_path)
            return self._historical

        # Download csv file from S3.
        source_path = self._source_path()
        self._download_s3_file(
            local_cache_path,
            source_path,
        )
        self._historical = pd.read_csv(local_cache_path)
        return self._historical

    @abstractmethod
    def _local_cache_path(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _source_path(self) -> str:
        raise NotImplementedError
