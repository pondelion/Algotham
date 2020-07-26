from abc import ABCMeta, abstractmethod

from ..algo_runner.algo_system import AlgoSystem


class BaseRule(metaclass=ABCMeta):

    def __init__(self, simulation_mode=False):
        self._simulation_mode = simulation_mode

    def set_context(
        self,
        system: AlgoSystem
    ) -> None:
        self._system = system

    @property
    def context(self):
        return self._system
