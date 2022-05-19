# Задание №4

new_list = []
ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('test_3.txt') as test_file:
    for i in test_file:
        i = i.split(' ', 1)
        new_list.append(ru[i[0]] + ' ' + i[1])
with open('test_3.1.txt', 'w') as test_file:
    test_file.writelines(new_list)