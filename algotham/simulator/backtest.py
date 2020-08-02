from datetime import datetime, timedelta

from ..algo import SimulatedAlgo


class BackTest:

    def __init__(
        self,
        algo_system: SimulatedAlgo,
    ):
        self._algo_system = algo_system

    def run(self, start_dt: datetime, end_dt: datetime):

        self._algo_system.reset()
        cur_dt = start_dt
        self._algo_system.set_time(start_dt, wait_update_reflected=False)

        self._algo_system.run()

        while cur_dt <= end_dt:
            self._algo_system.set_time(cur_dt)
            cur_dt += timedelta(minutes=1)
            # if cur_dt.minute == 0 and cur_dt.second == 0:
            #     print(cur_dt)

    def result(self):
        return self._algo_system.recorder
