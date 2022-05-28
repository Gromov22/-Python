#Задание №4


class Storehouse:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.total_info = {'Name': self.name, 'Amount': self.amount, 'Price': self.price}

    def __str__(self):
        return f'{self.total_info}'

    @staticmethod
    def to_store():
        result = []
        stop_word = False
        try:
            while not stop_word:
                name = input('Введите наименование товара: ')
                amount = int(input('Введите количество товара: '))
                price = int(input('Введите стоимость товара: '))
                on_go = input('Введите enter для продолжения или Q для выхода: ')
                info = {'Name': name, 'Amount': amount, 'Price': price}
                result.append(info)
                if on_go == 'Q' or on_go =='q':
                    stop_word = True
                    break
        except ValueError:
            print('Неверное значение')
        finally:
            return f'Добавлено на склад: {result}'


class Printer(Storehouse):
    paper = 100
    ink = 1000

    def __init__(self, name, amount, price):
        super().__init__(name, amount, price)

    @classmethod
    def to_print(cls, pages):
        print('печать идет'.upper())
        while cls.paper != 0 or cls.ink != 0:
            for i in range(pages):
                cls.paper -= 1
                cls.ink -= i * 2
                print(f'Запас бумаги: {cls.paper}, запас чернил: {cls.ink}')
                if cls.paper < 0:
                    print(f'Бумага закончилась.')
                    break
                elif cls.ink < 0:
                    print(f'Чернила закончились.')
                    break
                else:
                    continue
            return f'Печать завершена. Запас бумаги: {cls.paper}, запас чернил: {cls.ink}'


class Scanner(Storehouse):
    def __init__(self, name, amount, price):
        super().__init__(name, amount, price)

    @classmethod
    def to_scan(cls, amount):
        return f'Отсканировано страниц: {amount}'


class Copier(Storehouse):
    def __init__(self, name, amount, price):
        super().__init__(name, amount, price)

    @classmethod
    def to_copy(cls, amount):
        return f'Сделано копий: {amount}'


printer = Printer('HP', 1, 20000)
scanner = Scanner('Samsung', 1, 10000)
copier = Copier('Xerox', 1, 15000)

print(printer)
print(Printer.to_print(5))
print(Scanner.to_scan(5))
print(Copier.to_copy(5))
print(Storehouse.to_store())