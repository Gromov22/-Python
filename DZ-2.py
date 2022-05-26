# Задание №2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def get_score(self):
        pass

    def __add__(self, other):
        return f'Общий расход ткани составляет: {((self.size / 6 + 0.5) + (other.size * 2 + 0.3)).__round__(2)}м'


class Coat(Clothes, ABC):
    def __init__(self, size):
        super().__init__(size)

    @property
    def get_score(self):
        return f'Расход ткани на пальто составляет: {(self.size / 6.5 + 0.5).__round__(2)}м'


class Suit(Clothes, ABC):
    def __init__(self, size):
        super().__init__(size)

    @property
    def get_score(self):
        return f'Расход ткани на костюм составляет: {(self.size * 2 + 0.3).__round__(2)}м'


a = Coat(10)
b = Suit(1)
print(a.get_score)
print(b.get_score)
print(a + b)