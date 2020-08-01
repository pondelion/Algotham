from abc import ABCMeta, abstractmethod

# from ..algo.algo import Algo


class BaseRule(metaclass=ABCMeta):

    def __init__(self, simulation_mode=False):
        self._simulation_mode = simulation_mode

    def set_context(
        self,
        algo #: Algo
    ) -> None:
        self._algo = algo

    @property
    def context(self):
        return self._algo
