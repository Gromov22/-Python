# Задание №5

with open('test_4.txt', 'w+') as test_file:
    numbers = ['123 456 789 101112 131415']
    test_file.writelines(numbers)
    test_file.seek(0)
    for i in test_file:
        i = i.split()
        print(f'Result: {sum(map(int, i))}')