item_number = 0
book = []
item_comby = []
price_comby = []
quantity_comby = []
unit_comby = []
while True:
    item_number += 1
    catalog = {'Название': '', 'Цена': '', 'Количество': '', 'Ед.изм.': ''}
    catalog['Название'] = input('\nВведите название товара: ')
    while True:
        catalog['Цена'] = input('Введите цену товара: ')
        try:
            catalog['Цена'] = round(float(catalog['Цена']), 2)
            if catalog['Цена'] > 0:
                break
            else:
                continue
        except ValueError:
            continue
    while True:
        catalog['Количество'] = input('Введите количество товара: ')
        try:
            catalog['Количество'] = round(float(catalog['Количество']), 2)
            if catalog['Количество'] >= 0:
                break
            else:
                continue
        except ValueError:
            continue
    catalog['Ед.изм.'] = input('Введите единицу измерения: ')
    line = (item_number, catalog)
    book.append(line)
    print('\nКаталог теперь выглядит так:')

    for position in book:
        print(position)

    order_dict = catalog.copy()

    item_comby.append(order_dict['Название'])
    price_comby.append(order_dict['Цена'])
    quantity_comby.append(order_dict['Количество'])
    unit_comby.append(order_dict['Ед.изм.'])

    order_dict['Название'] = item_comby
    order_dict['Цена'] = price_comby
    order_dict['Количество'] = quantity_comby
    order_dict['Ед.изм.'] = unit_comby

    if item_number > 1:
        report = input('\nХотите вывести отчёт? (y/n)\n')
        if report == 'y':
            for i in order_dict.items():
                print(i[0], list(set(i[1])), sep=':')

    next_item = input('\nХотите ввести ещё одну позицию товара? (y/n)')
    if next_item == 'y':
        continue
    else:
        break
