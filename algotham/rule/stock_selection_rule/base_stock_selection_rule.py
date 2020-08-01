from abc import ABCMeta, abstractmethod
from typing import List
from datetime import datetime

from ..base_rule import BaseRule
from ...data.stock import Stock


class BaseStockSelectionRule(BaseRule, metaclass=ABCMeta):

    @abstractmethod
    def select_stocks(self, dt: datetime) -> List[Stock]:
        raise NotImplementedError
