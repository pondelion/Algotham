from abc import ABCMeta, abstractmethod

from ..base_rule import BaseRule


class BaseVolumeRule(BaseRule, metaclass=ABCMeta):

    @abstractmethod
    def decice_volume(self, stock: Stock) -> int:
        raise NotImplementedError
