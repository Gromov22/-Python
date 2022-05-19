# Задание №1

try:
    with open('text.txt', 'w+') as test_file:
        while True:
            content = input('Введите данные: ')
            test_file.writelines(content)
            if not content:
                break
        test_file.seek(0)
        for line in test_file:
            print(line)
except IOError:
    print('Ошибка ввода-вывода!')