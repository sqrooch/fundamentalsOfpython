# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            self.is_police = 'Полицейский автомобиль'
        else:
            self.is_police = 'Гражданский автомобиль'
        print(f'{self.is_police}. {self.color} {self.name}. Скорость {self.speed}.')

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} двигается со скоростью {self.speed}')

    def stop(self):
        print(f'{self.name} остановился')
        self.speed = 0

    def turn(self, direction):
        if self.speed != 0:
            print(f'{self.name} повернул {direction}')
        else:
            print(f'{self.name} не может повернуть. Машина остановлена.')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость')
        else:
            print(f'Скорость {self.name} равна {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость')
        else:
            print(f'Скорость {self.name} равна {self.speed}')


class PoliceCar(Car):
    pass


audi = TownCar(50, 'Чёрный', 'Audi', False)
audi.stop()
audi.turn('налево')
audi.go(60)
audi.go(80)
audi.turn('направо')
audi.show_speed()
audi.stop()
audi.show_speed()

vaz = PoliceCar(60, 'Синий', 'ВАЗ', True)
alfa = SportCar(100, 'Красный', 'AlfaRomeo', False)
kamaz = WorkCar(30, 'Белый', 'Камаз', False)

kamaz.go(80)
audi.show_speed()
kamaz.show_speed()
alfa.turn('налево')
vaz.stop()
vaz.turn('назад')

# Это очень интересная задача.
# Она раскрывает весь смысл ООП.