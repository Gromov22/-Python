# Задание №6
analytics = []
for i in range(1, 4):
    product = (i, {'Название': input('Введите название товара: '), 'Цена': int(input('Введите стоимость товара: ',)),
               'Количество': int(input('Введите количество товара: ')), 'Ед': input('Введите единицу измерения: ')})
    analytics.append(product)
for ind, el in enumerate(analytics):
    print(el)

result = {'Название':  [analytics[0][1].get('Название'), analytics[1][1].get('Название'), analytics[2][1].get('Название')],
          'Цена': [analytics[0][1].get('Цена'), analytics[1][1].get('Цена'), analytics[2][1].get('Цена')],
          'Количество': [analytics[0][1].get('Количество'), analytics[1][1].get('Количество'), analytics[2][1].get('Количество')],
          'Ед': [analytics[0][1].get('Ед'), analytics[1][1].get('Ед'), analytics[2][1].get('Ед')]}
for ind, el in enumerate(result.items()):
    print(el)
