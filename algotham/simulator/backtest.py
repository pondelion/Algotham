from datetime import datetime, timedelta

from ..algo import SimulatedAlgo


class BackTest:

    def __init__(
        self,
        algo_system: SimulatedAlgo,
        start_dt: datetime,
        end_dt: datetime
    ):
        self._algo_system = algo_system
        self._start_dt = start_dt
        self._end_dt = end_dt

    def run(self):

        cur_dt = self._start_dt
        self._algo_system.set_time(self._start_dt, wait_update_reflected=False)

        self._algo_system.run()

        while cur_dt <= self._end_dt:
            self._algo_system.set_time(cur_dt)
            cur_dt += timedelta(minutes=1)
            # if cur_dt.minute == 0 and cur_dt.second == 0:
            #     print(cur_dt)

    def result(self):
        return self._algo_system.recorder
