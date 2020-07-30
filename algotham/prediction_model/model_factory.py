from enum import Enum

from .random_model import RandomModel


class ModelType(Enum):

    RANDOM = RandomModel


class ModelFactory:

    @staticmethod
    def get_model(
        model_type: ModelType
    ):
        return model_type.value()
