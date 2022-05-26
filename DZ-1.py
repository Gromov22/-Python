# Задание №1

class Matrix:
    def __init__(self, *lines):
        self.lines = lines

    def __add__(self, other):
        return Matrix([[self.lines[i][k] + other.lines[i][k] for i in range(len(self.lines))]
                       for k in range(len(self.lines))])

    def __str__(self):
        return f'{self.lines}'.replace('([[', '').replace('], [', '\n').replace(']],)', '')


a = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
b = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])
print(a + b)