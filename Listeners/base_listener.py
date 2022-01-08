from abc import ABC, abstractmethod

class BaseListener(ABC):

    @abstractmethod
    def handle(self):
        pass

    def __call__(self, event=None):
        self.handle()