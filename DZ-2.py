# Задание №2

def user_info(**kwargs):
    return kwargs
print(user_info(name = input('Введите имя: '), surname = input('Введите фамилию: '), age = int(input('Введите возраст: ')),
                birth_year = int(input('Введите год рождения: ')), town = input('Введите город проживания: '),
                email = input('Введите email: '), phone = input('Введите номер телефона: ')))
