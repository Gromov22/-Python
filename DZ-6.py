# Задание №6

from itertools import count

for i in count(int(input('Введите начальное число'))):
    i += 1
    if i > 10:
        break
    print(i)

from itertools import cycle

a = 0
my_list = [3, 'hundred', '$']
for i in cycle(my_list):
    a += 1
    if a > 12:
        break
    print(i)