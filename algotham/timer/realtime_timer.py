from datetime import datetime

from overrides import overrides

from .base_timer import BaseTimer


class RealtimeTimer(BaseTimer):

    @overrides
    def get_time(self) -> datetime:
        self._update()
        return super.get_time()

    def _update(self) -> None:
        self._datetime = datetime.now()
