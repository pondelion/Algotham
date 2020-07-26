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
        algo: BaseAlgo,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
    ):
        super().init(
            algo,
            timing_rule,
            stock_selection_rule,
            volume_rule,
            SimulatedTimer()
        )

    def set_time(self, dt: datetime) -> None:
        self.timer.set_time(dt)
