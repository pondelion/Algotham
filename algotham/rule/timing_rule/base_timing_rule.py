from abc import ABCMeta, abstractmethod

from ..base_rule import BaseRule


class BaseTimingRule(BaseRule, metaclass=ABCMeta):

    @abstractmethod
    def wait_for_next(self):
        raise NotImplementedError
