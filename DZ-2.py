# Задание №2


class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


user_input_1 = int(input('Введите числo a: '))
user_input_2 = int(input('Введите числo b: '))

try:
    if user_input_2 == 0:
        raise OwnException('Деление на ноль!')
except OwnException as err:
    print(err)
else:
    print(f'Результат: {user_input_1 / user_input_2}')
#