# Задание №2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def score(self, asphalt_weight, asphalt_thickness):
        print('Масса асфальта в тоннах:')
        return (self._length * self._width * asphalt_weight * asphalt_thickness) // 1000


result = Road(20, 5000)
print(result.score(25, 5))