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
from ..transact import (
    BaseTransaction,
    DefaultTransaction
)


class Algo:

    def __init__(
        self,
        timing_rule: BaseTimingRule,
        stock_selection_rule: BaseStockSelectionRule,
        volume_rule: BaseVolumeRule,
        init_portfolio: Portfolio = Portfolio(),
        transaction: BaseTransaction = DefaultTransaction(),
        timer: BaseTimer = RealtimeTimer()
    ):
        self._timing_rule = timing_rule
        self._stock_selection_rule = stock_selection_rule
        self._volume_rule = volume_rule
        self._timer = timer
        self._transaction = transaction
        self._timing_rule.set_context(self)
        self._stock_selection_rule.set_context(self)
        self._volume_rule.set_context(self)
        self._transaction.set_context(self)
        self._recorder = Recorder()
        self._portfolio = init_portfolio
        self._updated = False

    def run(self):
        self._thread = threading.Thread(
            target=self._run
        )
        self._thread.start()

    def _run(self):
        while True:
            self._timing_rule.wait_for_next()

            selected_stocks = self._stock_selection_rule.select_stocks(
                self.timer.get_time()
            )

            for stock in selected_stocks:
                dt = self.timer.get_time()
                volume = self._volume_rule.decide_volume(
                    stock, dt
                )
                self._transaction.transact(
                    dt,
                    stock,
                    volume
                )

    @property
    def timer(self):
        return self._timer

    @property
    def recorder(self):
        return self._recorder

    @property
    def portfolio(self):
        return self._portfolio
