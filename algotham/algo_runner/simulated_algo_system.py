import time
from datetime import datetime

from .algo_system import AlgoSystem
from ..algo.base_algo import BaseAlgo
from ..rule import (
    BaseTimingRule,
    BaseStockSelectionRule,
    BaseVolumeRule
)
from ..timer import (
    BaseTimer,
    SimulatedTimer,
)


class SimulatedAlgoSystem(AlgoSystem):

    def __init__(
        self,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
    ):
        super().init(
            timing_rule,
            stock_selection_rule,
            volume_rule,
            SimulatedTimer()
        )

    def set_time(self, dt: datetime) -> None:
        self.timer.set_time(dt)
        self._updated = False
        while not self._updated:
            time.sleep(0.001)
