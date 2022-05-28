# Задание №7

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Result: {self.a + other.a}+{self.b + other.b}i'.replace('+', '' if self.b + other.b < 0 else '+')

    def __mul__(self, other):
        return f'Result: {self.a * other.a + self.b * other.a}+{self.a * other.b + self.b * other.b}i'.replace('+', ''
                if self.a * other.b + self.b * other.b < 0 else '+')


a = Complex(1, 3)
b = Complex(4, -5)

print(a + b)
print(a * b)