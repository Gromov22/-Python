# Задание №1

class Date:
    day = []
    month = []
    year = []
    # result = []

    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def int_type(cls, date):
        cls.day = [el for i, el in enumerate(date) if i < 2]
        cls.month = [el for i, el in enumerate(date) if 2 < i < 5]
        cls.year = [el for i, el in enumerate(date) if i > 5]
        return int(''.join(cls.day)), int(''.join(cls.month)), int(''.join(cls.year))
        # return list(map(int, (''.join(cls.day), ''.join(cls.month), ''.join(cls.year)))) - возвращает список

    # def int_type(cls, date):
    #     for i in date.split():
    #         if i.isdigit():
    #             cls.result.append(i)
    #     return int(cls.result[0]), int(cls.result[1]), int(cls.result[2])
    # тоже вариант, но не работает с форматом dd.mm.yyyy, приходится делать dd - mm - yyyy

    @staticmethod
    def validation(day, month, year):
        if day == 0 or day > 31:
            return f'Неверный параметр дня'
        elif month == 0 or month > 12:
            return f'Неверный параметр месяца'
        elif year > 2022:
            return f'Быть такого не может'
        else:
            return f'Все хорошо, ваша дата: {day}.{month}.{year}'


print(Date.int_type('22.03.2000'))
print(Date.validation(22, 3, 2000))