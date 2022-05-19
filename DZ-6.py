# Задание №6

with open('test_5.txt') as test_file:
    for line in test_file:
        line = line.replace('(', ' ').split()
        lessons = {line[0]: sum([int(i) for i in line if i.isdigit()])}
        print(lessons)