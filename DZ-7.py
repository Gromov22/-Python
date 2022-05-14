# Задание №7
from itertools import count
from math import factorial

def fact(n):
    for el in count(1):
        yield factorial(el)
        if el == n:
            break

for el in fact(10):
    print(el)