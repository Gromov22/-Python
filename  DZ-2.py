# Задание №2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [i for el, i in enumerate(my_list) if my_list[el - 1] < my_list[el]]
print(f'Старый список: {my_list}')
print(f'Новый список: {new_list}')