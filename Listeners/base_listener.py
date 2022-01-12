from abc import ABC, abstractmethod

class BaseListener(ABC):

    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def build():
        pass

    def __call__(self):
        self.handle()