from abc import ABCMeta, abstractmethod
from datetime import datetime


class BaseTimer(metaclass=ABCMeta):

    def get_time(self) -> datetime:
        return self._datetime
