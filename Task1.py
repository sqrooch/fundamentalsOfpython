# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

import time
import sys


class TrafficLight:
    def __init__(self, color):
        self.__color = color
        self.__new_color = ''

        if self.__color == 'red':
            print('\nСветофор горит КРАСНЫМ, подождите!')
            time.sleep(7)
        elif self.__color == 'yellow':
            print('\nСветофор горит ЖЁЛТЫМ, подождите!')
            time.sleep(2)
        elif self.__color == 'green':
            print('\nСветофор горит ЗЕЛЁНЫМ, подождите!')
            time.sleep(5)
        else:
            print('\nВведено неверное значение')
            sys.exit()

    def running(self):
        while True:
            self.__new_color = input('красный - "red"\nжёлтый - "yellow"\nзелёный - "green"\nВведите режим светофора: ')
            if self.__color == 'red' and self.__new_color == 'yellow':
                print('\nСветофор горит ЖЁЛТЫМ, подождите!')
                time.sleep(2)
                self.__color = self.__new_color
            elif self.__color == 'yellow' and self.__new_color == 'green':
                print('\nСветофор горит ЗЕЛЁНЫМ, подождите!')
                time.sleep(5)
                self.__color = self.__new_color
            elif self.__color == 'green' and self.__new_color == 'red':
                print('\nСветофор горит КРАСНЫМ, подождите!')
                time.sleep(7)
                self.__color = self.__new_color
            else:
                print('\nВы не соблюли порядок светофора. Выход.')
                break


instruction = TrafficLight(input('красный - "red"\nжёлтый - "yellow"\nзелёный - "green"\nВведите режим светофора: '))
instruction.running()
