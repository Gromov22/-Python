# Задание №1

import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self, time_red, time_yellow, time_green):
        while True:
            print(self.__color[0])
            time.sleep(time_red)
            print(self.__color[1])
            time.sleep(time_yellow)
            print(self.__color[2])
            time.sleep(time_green)


a = TrafficLight()
print(a.running(7, 2, 5))