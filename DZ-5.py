# Задание №5

proceeds = int(input('Укажите выручку фирмы'))
costs = int(input('Укажите издержки фирмы'))

if proceeds > costs:
    print('Ваша выручка больше издержек')
    n = proceeds - costs
    print(f'Ваша прибыль составляет {n}')
    employees = int(input('Укажите количество сотрудников'))
    profit = n / proceeds / employees
    print(f'Рентабельность фирмы в расчете на одного сотрудника составляет {profit}')
else:
    print('Ваши издержки больше прибыли')
    n = costs - proceeds
    print(f'Ваш убыток составляет {n}')