from datetime import datetime
from abc import ABCMeta, abstractmethod


class BaseAlgo(metaclass=ABCMeta):

    @abstractmethod
    def predict(
        self,
        company_code: int,
        dt: datetime,
    ) -> float:
        raise NotImplementedError

    @abstractmethod
    def train(self):
        raise NotImplementedError
