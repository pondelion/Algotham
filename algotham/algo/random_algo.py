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
        return 1.0 if random.rand() > 0.5 else -1.0

    @overrides
    def train(self):
        pass
