# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.

# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).

# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position):
        wage = 50
        bonus = 200
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        print(f'{self.name} {self.surname} - {self.position}')


class Position(Worker):
    def get_full_name(self):
        print('Имя сотрудника -', self.surname, self.name)

    def get_total_income(self):
        print('Доход сотрудника составляет:', self._income.get('wage') + self._income.get('bonus'), 'руб.')


worker = Position('Скрудж', 'МакДак', 'Президент компании')
worker.get_full_name()
worker.get_total_income()
