# Задание №3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        print(f'Занимаемая должность: {self.position}')
        return sum(self._income.values())


worker_info = Position('David', 'Bowie', 'Starman', 100, 200)

print(worker_info.get_full_name())
print(worker_info.get_total_income())