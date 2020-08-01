import os
import time

from overrides import overrides

from .observer import Observer


class FileObserver(Observer):

    def __init__(self, filepath: str):
        self._filepath = filepath
        self._last_updated = os.path.getmtime(self._filepath)

    @overrides
    def _observe(self):
        while self._stop is False:
            last_updated = os.path.getmtime(self._filepath)
            if last_updated != self._last_updated:
                self._call_listeners()
                self._last_updated = last_updated
            time.sleep(self._observation_interval_sec)

        self._stop = False

    def _call_listeners(self):
        for listener in self._listeners:
            listener.on_file_update()
