from abc import ABCMeta, abstractmethod
from datetime import datetime


class BaseTimer(metaclass=ABCMeta):

    def __init__(
        self,
        init_dt: datetime = datetime.now(),
    ):
        self._datetime = init_dt

    def get_time(self) -> datetime:
        return self._datetime
