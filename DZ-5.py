# Задание №5

from functools import reduce


def my_func(x, y):
    return x * y


print(reduce(my_func, [i * i for i in range(100, 1001) if i % 2 == 0]))