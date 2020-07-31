from abc import ABCMeta, abstractmethod


class FileUpdateListener(Listener):

    @abstractmethod
    def on_file_update(self):
        raise NotImplementedError
