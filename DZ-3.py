# Задание №3

class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count) if self.count > other.count else f'Negative cell count'

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __str__(self):
        return f'Result: {self.count}'

    def make_order(self, cells_in_row):
        row = str().join(f'{"*" * cells_in_row}\\n' for i in range(self.count // cells_in_row))\
              + f'{"*" * (self.count % cells_in_row)}'
        return f'Cells in a row: {row}'


a = Cell(13)
b = Cell(15)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))
print(b.make_order(5))