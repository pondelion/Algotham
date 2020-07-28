from abc import ABCMeta, abstractmethod
from datetime import datetime
import time

from ..base_rule import BaseRule


class BaseTimingRule(BaseRule, metaclass=ABCMeta):

    @abstractmethod
    def wait_for_next(self):
        raise NotImplementedError

    def wait_until(self, until_dt: datetime) -> None:

        if self.context is None:
            raise Exception('system is not set')

        while self.context.timer.get_time() < until_dt:
            self.context._updated = True
            time.sleep(0.01)
