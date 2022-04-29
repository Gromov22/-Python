# Задание №5
def sum_func():
    a = 0
    stop_word = False
    while not stop_word:
        source = input('Введите строку чисел или Q для выхода: ').split()
        if source[0] == 'Q' or source[0] == 'q':
            stop_word = True
            print('Сессия окончена')
        else:
            result = sum([int(i) for i in source])
            a += result
            print(f'Текущее значение = {result}')
            print(f'Общая сумма = {a}')
print(sum_func())