from abc import ABCMeta, abstractmethod
from typing import List

from ..base_rule import BaseRule
from ...data.stock import Stock


class BaseStockSelectionRule(BaseRule, metaclass=ABCMeta):

    @abstractmethod
    def select_stocks(self) -> List[Stock]:
        raise NotImplementedError
