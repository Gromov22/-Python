#Задание №5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'.upper()


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Ваш инструмент - {self.title}\nЗапуск отрисовки ручкой...'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Ваш инструмент - {self.title}\nЗапуск отрисовки карандашом...'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Ваш инструмент - {self.title}\nЗапуск отрисовки маркером...'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

a = Stationery(None)
print(a.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
