from ..algo.base_algo import BaseAlgo
from ..rule import (
    BaseTimingRule,
    BaseStockSelectionRule,
    BaseVolumeRule
)
from ..timer import (
    BaseTimer,
    RealtimeTimer
)


class AlgoSystem:

    def __init__(
        self,
        algo: BaseAlgo,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
        timer: BaseTimer = RealtimeTimer()
    ):
        self._algo = algo
        self._timing_rule = timing_rule
        self._stock_selection_rule = stock_selection_rule
        self._volume_rule = volume_rule
        self._timer = timer
        self._timing_rule.set_context(self)
        self._stock_selection_rule.set_context(self)
        self._volume_rule.set_context(self)

    def run(self):

        while True:
            self._timing_rule.wait_for_next()

            selected_stocks = self._stock_selection_rule.select_stocks()

            for stock in selected_stocked:
                volume = self._volume_rule.decide_volume(stock)

    @property
    def timer(self):
        return self._timer