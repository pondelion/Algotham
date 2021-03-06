from abc import ABCMeta, abstractmethod
from datetime import datetime


class BaseModel(metaclass=ABCMeta):

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
