from abc import ABCMeta, abstractmethod
import threading


class Observer(metaclass=ABCMeta):

    def __init__(self):
        self._listeners = []
        self._thread = None
        self._stop = False
        self._observation_interval_sec = 60

    def regist_listener(self, listener: Listener) -> None:
        self._listeners.append(listenr)

    def remove_listener(self, listener: Listener) -> bool:
        self._listeners.remove(listener)

    def observe(self) -> None:
        self._thread = threading.Thread(
            target=self._observe
        )
        self._thread.start()
        self._stop = False

    def stop(self) -> None:
        if self._thread is None:
            return
        self._stop = True
        self._thread = None

    @abstractmethod
    def _observe(self):
        raise NotImplementedError
