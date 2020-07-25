from datetime import datetime

from .base_timer import BaseTimer


class SimulatedTimer(BaseTimer):

    def set_time(dt: datetime) -> None:
        self._datetime = dt
