import threading

from ..rule.timing_rule.base_timing_rule import BaseTimingRule
from ..rule.stock_selection_rule.base_stock_selection_rule import BaseStockSelectionRule
from ..rule.volume_rule.base_volume_rule import BaseVolumeRule
from ..timer import (
    BaseTimer,
    RealtimeTimer
)
from ..portfolio import Portfolio
from ..data.stock import Stock
from ..recorder import Recorder


class Algo:

    def __init__(
        self,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
        init_portfolio: Portfolio,
        timer: BaseTimer = RealtimeTimer()
    ):
        self._timing_rule = timing_rule
        self._stock_selection_rule = stock_selection_rule
        self._volume_rule = volume_rule
        self._timer = timer
        self._timing_rule.set_context(self)
        self._stock_selection_rule.set_context(self)
        self._volume_rule.set_context(self)
        self._recorder = Recorder()
        self._updated = False

    def run(self):
        self._thread = threading.Thread(
            target=self._run
        )
        self._thread.start()

    def _run(self):
        while True:
            self._timing_rule.wait_for_next()

            selected_stocks = self._stock_selection_rule.select_stocks()

            for stock in selected_stocks:
                volume = self._volume_rule.decide_volume(
                    stock,
                    self.timer.get_time()
                )
                if self._transact(stock, volume):
                    pass

    @property
    def timer(self):
        return self._timer

    @property
    def recorder(self):
        return self._recorder

    def _transact(
        self,
        stock: Stock,
        volume: int
    ) -> bool:
        pass
