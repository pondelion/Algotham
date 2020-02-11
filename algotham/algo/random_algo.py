import random
from datetime import datetime

from overrides import overrides

from .base_algo import BaseAlgo


class RandomAlgo(BaseAlgo):

    @overrides
    def predict(
        self,
        company_code: int,
        dt: datetime,
    ) -> float:
        return random.rand() > 0.5

    @overrides
    def train(self):
        pass
