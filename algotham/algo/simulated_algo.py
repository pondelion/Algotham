import time
from datetime import datetime

from .algo import Algo
from ..rule import (
    BaseTimingRule,
    BaseStockSelectionRule,
    BaseVolumeRule
)
from ..timer import (
    BaseTimer,
    SimulatedTimer,
)
from ..portfolio import Portfolio


class SimulatedAlgo(Algo):

    def __init__(
        self,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
        init_portfolio: Portfolio = Portfolio(),
    ):
        super().__init__(
            timing_rule,
            stock_selection_rule,
            volume_rule,
            init_portfolio,
            SimulatedTimer()
        )

    def set_time(
        self,
        dt: datetime,
        force_update=False
    ) -> None:
        self.timer.set_time(dt)
        if force_update:
            return
        self._updated = False
        while not self._updated:
            time.sleep(0.0001)
