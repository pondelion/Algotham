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
from ..transact import (
    BaseTransaction,
    DefaultTransaction
)


class SimulatedAlgo(Algo):

    def __init__(
        self,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
        init_portfolio: Portfolio = Portfolio(),
        transaction: BaseTransaction = DefaultTransaction(),
    ):
        super().__init__(
            timing_rule,
            stock_selection_rule,
            volume_rule,
            init_portfolio,
            transaction,
            SimulatedTimer()
        )

    def set_time(
        self,
        dt: datetime,
        wait_update_reflected=True
    ) -> None:
        self.timer.set_time(dt)
        if not wait_update_reflected:
            return
        self._updated = False
        while not self._updated:
            time.sleep(0.0001)
