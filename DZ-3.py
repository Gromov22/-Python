class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
stop_word = False

while not stop_word:
    try:
        user_input = input('Введите данные или Q для выхода: ')
        if user_input.isdigit():
            my_list.append(int(user_input))
        elif user_input == 'Q' or user_input == 'q':
            stop_word = True
            print(f'Ваш список: {my_list}')
            break
        else:
            raise OwnError('Вы ввели неверное значение!')
    except OwnError as err:
        print(err)