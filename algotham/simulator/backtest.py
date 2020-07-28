from datetime import datetime, timedelta


class BackTest:

    def __init__(
        self,
        algo_system: SimulatedAlgoSystem,
        start_dt: datetime,
        end_dt: datetime
    ):
        self._algo_system = algo_system
        self._start_dt = start_dt
        self._end_dt = end_dt

    def run(self):

        cur_dt = self._start_dt

        while cur_dt <= self._end_dt:
            self._algo_system.set_time(cur_dt)
            cur_dt += timedelta(minutes=1)

    def result(self):
        return self._algo_system.record
