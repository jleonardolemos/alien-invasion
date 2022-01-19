from abc import ABC, abstractmethod

class Updateable(ABC):

    @abstractmethod
    def update(self):
        pass