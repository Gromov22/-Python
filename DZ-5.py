# Задание №5

def sum_func():
    result = 0
    stop_word = False
    while not stop_word:
        source = input('Введите строку чисел или Q для выхода: ').split()
        current = 0
        for el in range(len(source)):
            if source[el] == 'Q' or source[el] == 'q':
                stop_word = True
                print('Сессия окончена'.upper())
                break
            else:
                current += int(source[el])
        result += current
        print(f'Текущая сумма = {current}')
        print(f'Общая сумма = {result}')