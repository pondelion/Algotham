from abc import ABCMeta, abstractmethod
import os

import pandas as pd

from ..storage import S3


cache = {}


class CSVHistoricalData(metaclass=ABCMeta):

    @property
    def historical(self) -> pd.DataFrame:
        return self._histrical()

    def _historical(self):

        local_cache_path = self._local_cache_path()

        if local_cache_path in cache:
            return cache[local_cache_path]

        # If cache file already exists, use it.
        if os.path.exists(local_cache_path):
            cache[local_cache_path] = pd.read_csv(local_cache_path)
            return cache[local_cache_path]

        # Download csv file from S3.
        source_path = self._source_path()
        self._download_s3_file(
            local_cache_path,
            source_path,
        )
        cache[local_cache_path] = pd.read_csv(local_cache_path)
        return cache[local_cache_path]

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
        S3.download_file(source_path, local_dest_path)
