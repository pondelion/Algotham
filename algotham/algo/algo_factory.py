from enum import Enum

from . import random_algo


class AlgoType(Enum):

    RANDOM = getattr(random_algo, 'RandomAlgo')


class AlgoFactory:

    @staticmethod
    def get_algo(
        algo_type: AlgoType
    ):
        return algo_type.value()
