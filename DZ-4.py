# Задание №4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed}км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed}км/ч' if self.speed <= 60 else f'{self.name} движется со скоростью, превышающей допустимую'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed}км/ч' if self.speed <= 40 else f'{self.name} движется со скоростью, превышающей допустимую'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'Red', 'Mazda', False)
sport_car = SportCar(130, 'Black', 'Maserati', False)
work_car = WorkCar(40, 'White', 'Toyota', False)
police_car = PoliceCar(60, 'Blue', 'Mercedes-Benz', True)

print(town_car.show_speed())
print(sport_car.show_speed())
print(work_car.name)
print(police_car.is_police)
print(sport_car.color)
print(town_car.go(), sport_car.stop(), police_car.turn_right(), work_car.turn_left())