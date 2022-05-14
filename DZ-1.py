# Задание №1

from sys import argv

try:
    name, time, salary, bonus = argv
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = time * salary + bonus
    print(f'Сотрудник заработал: {result}')
except ValueError:
    print('Неверное значение')