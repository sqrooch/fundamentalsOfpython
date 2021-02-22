# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def showing(self):
        pass

    def __add__(self, other):
        print(f'На них уйдёт {Coat.textile(self.name, size) + Costume.textile(other.name, height)} пог.м ткани.')


class Coat(Clothes):

    @property
    def showing(self):
        return self.name

    def textile(self, size):
        return round(size / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def showing(self):
        return self.name

    def textile(self, height):
        return round(2 * height / 100 + 0.3, 2)


coat_model1 = Coat('пальто (модель №1)')
coat_model2 = Coat('пальто (модель №2)')
coat_model3 = Coat('пальто (модель №3)')

coat_models = {1: coat_model1, 2: coat_model2, 3: coat_model3}

costume_model1 = Costume('костюм (модель №1)')
costume_model2 = Costume('костюм (модель №2)')

costume_models = {1: costume_model1, 2: costume_model2}

print('В магазине представлено три модели пальто.')
coat_model = int(input('Выберите номер модели пальто: '))
size = int(input('Введите свой размер: '))
print(f'Расход ткани на пальто составит {coat_models.get(coat_model).textile(size)} пог.м.')

print('\nВ магазине также представлены две модели костюма.')
costume_model = int(input('Выберите номер модели костюма: '))
height = int(input('Введите свой рост(см): '))
print(f'Расход ткани на костюм составит {costume_models.get(costume_model).textile(height)} пог.м.')

print(f'\nВы выбрали {coat_models.get(coat_model).showing} и {costume_models.get(costume_model).showing}.')
coat_models.get(coat_model).__add__(costume_models.get(costume_model))
