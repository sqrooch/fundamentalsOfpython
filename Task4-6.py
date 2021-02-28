# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
# постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
# ООП.

""" Это часть от задания 4. По условию, она не пригождается в задаче по складу.
    Закоментировал, чтобы не мешалась.

class Equipment:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color


class Printer(Equipment):
    def printer_func(self, tech_type):
        pass


class Scanner(Equipment):
    def scanner_func(self, page_format):
        pass


class Fax(Equipment):
    def fax_func(self, transfer_time):
        pass
"""

items = []  # Список товаров на складе. По умолчанию склад пуст.


def valid_id():
    while True:
        in_dict = 'missed'
        input_id = input('Введите id товара для операции: ')
        for _ in suppliers_items.keys():
            if input_id == _:
                in_dict = 'hit'  # Есть совпадение с id товара из номенклатуры.
        if in_dict == 'hit':
            return suppliers_items.get(input_id)
        else:
            print('Такого товара нет в номенклатуре.')


def valid_vol():
    while True:
        input_volume = input('Введите количество товара для операции: ')
        if input_volume.isdigit() and int(input_volume) > 0:
            return int(input_volume)
        else:
            print('Вы ввели неверные данные.')


def valid_dep():
    input_department = input('Введите название или номер департамента для отправки товара: ')
    return input_department


class Wh:
    def __init__(self, items_in_wh):
        self.items_in_wh = items_in_wh  # Переменная, которая отвечает за состояние склада в любой момент времени.

    def check_items(self):  # Проверяет состояние позиций на складе.
        print('\nПозиции на складе в данный момент:')
        if len(self.items_in_wh) == 0:
            print('Склад пуст.\n')
        else:
            [self.items_in_wh.remove(_) for _ in self.items_in_wh[:] if _['volume'] == 0]
            if len(self.items_in_wh) == 0:
                print('Склад пуст.\n')
            else:
                [print(_) for _ in self.items_in_wh]

    def arrival(self, id, volume):
        """Отвечает за поступление товара на склад.
                                                  Принимает id товара и количество позиций."""
        print(f'Склад совершил приёмку товара {id.setdefault("name")} марки {id.setdefault("brand")} '
              f'в количестве {volume} штук.')
        if len(self.items_in_wh) == 0:
            id['volume'] = volume
            self.items_in_wh.append(id)
        else:
            in_dict = ''
            for _ in self.items_in_wh:
                if _.setdefault('id') == id.setdefault('id'):
                    id['volume'] = _.setdefault('volume') + volume
                    return self.items_in_wh
                else:
                    in_dict = 'missed'  # Нет совпадений по id в словарях.
            if in_dict == 'missed':
                id['volume'] = volume
                self.items_in_wh.append(id)

    def distribution(self, id, volume, department):
        """Отвечает за распределение товаров между департаментами.
                Принимает id товара, количество позиций и название департамента, который сделал запрос на оргтехнику."""
        in_dict = 'missed'
        for _ in self.items_in_wh:
            if _.setdefault('id') == id.setdefault('id'):
                in_dict = 'hit'  # Нашёл совпадение по словарям.
                if _.setdefault('volume') < volume:
                    print(
                        f'Отгрузить {volume} штук {id.setdefault("name")} марки {id.setdefault("brand")} не удалось,'
                        f' потому что товара недостаточно на складе.')
                else:
                    _['volume'] = _.setdefault('volume') - volume
                    print(f'В отдел {department} отгружен {id.setdefault("name")} марки {id.setdefault("brand")} '
                          f'в количестве {volume} штук.')
                    return self.items_in_wh
        if in_dict == 'missed':  # Нет совпадений со словарями.
            print(f'Отгрузка {id.setdefault("name")} марки {id.setdefault("brand")} не удалась, '
                  f'потому что такого товара нет на складе.')


# Здесь представлен ассортимент, который могут предложить поставщики.
item1 = {'id': '001', 'name': 'printer', 'brand': 'Ricoh', 'color': 'black', 'tech_type': 'jet'}
item2 = {'id': '002', 'name': 'printer', 'brand': 'Hitachi', 'color': 'white', 'tech_type': 'matrix'}
item3 = {'id': '003', 'name': 'scanner', 'brand': 'Panasonic', 'color': 'black', 'page_format': 'A4'}
item4 = {'id': '004', 'name': 'scanner', 'brand': 'Hitachi', 'color': 'white', 'page_format': 'A3'}
item5 = {'id': '005', 'name': 'fax', 'brand': 'Sony', 'color': 'black', 'transfer_time': '10'}
item6 = {'id': '006', 'name': 'fax', 'brand': 'Panasonic', 'color': 'white', 'transfer_time': '12'}
suppliers_items = {'001': item1, '002': item2, '003': item3, '004': item4, '005': item5, '006': item6}

# Здесь вы можете задать алгоритм управления складом через команду Wh(items).
# Выбирая методы. Вы можете управлять складом.
# Метод .check_items() - обновляет данные по количеству товара на складе.
# Метод .arrival(valid_id(), valid_vol()) - закупает на склад товары из ассортимента поставщиков, представленном выше.
# Метод .distribution(valid_id(), valid_vol(), valid_dep()) - направляет товар со склада в указанный департамент.

Wh(items).check_items()
Wh(items).arrival(valid_id(), valid_vol())
Wh(items).arrival(valid_id(), valid_vol())
Wh(items).arrival(valid_id(), valid_vol())
Wh(items).check_items()
Wh(items).distribution(valid_id(), valid_vol(), valid_dep())
Wh(items).distribution(valid_id(), valid_vol(), valid_dep())
Wh(items).distribution(valid_id(), valid_vol(), valid_dep())
Wh(items).check_items()
