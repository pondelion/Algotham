from abc import ABCMeta, abstractmethod
from datetime import datetime

from ..base_rule import BaseRule
from ...data.stock import Stock


class BaseVolumeRule(BaseRule, metaclass=ABCMeta):

    @abstractmethod
    def decice_volume(
        self,
        stock: Stock,
        dt: datetime
    ) -> int:
        raise NotImplementedError
