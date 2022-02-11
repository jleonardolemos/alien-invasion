from abc import ABC, abstractmethod

class BaseGun(ABC):

    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def clean_bullets():
        pass

    @abstractmethod
    def get_bullets():
        pass

    @abstractmethod
    def get_bullets_copy():
        pass

    @abstractmethod
    def remove_bullet():
        pass
