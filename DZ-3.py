# Задание №3

with open('test_2.txt') as test_file:
    salary = []
    poor = []
    for line in test_file:
        line = line.split()
        salary.append(int(line[1]))
        if int(line[1]) < 20000:
            poor.append(line[0])
    print(f'Бедолаги: {poor}')
    print(f'Средняя зарплата: {sum(salary) / len(salary)}')