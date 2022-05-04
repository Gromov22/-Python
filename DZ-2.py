# Задание №2

def user_info(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(user_info(surname='Gromov', name='Aleksandr', year='2000', city='Moscow', email='error@mail.ru',
              telephone='8-800-123-45-67'))
