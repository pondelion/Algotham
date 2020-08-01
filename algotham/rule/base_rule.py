from abc import ABCMeta, abstractmethod

# from ..algo.algo import Algo


class BaseRule(metaclass=ABCMeta):

    def set_context(
        self,
        algo #: Algo
    ) -> None:
        self._algo = algo

    @property
    def context(self):
        return self._algo
