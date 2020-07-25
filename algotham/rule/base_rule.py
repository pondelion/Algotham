from abc import ABCMeta, abstractmethod


class BaseRule(metaclass=ABCMeta):

    def __init__(self, simulation_mode=False):
        self._simulation_mode = simulation_mode

    @abstractmethod
    def wait_for_next(self):
        raise NotImplementedError
