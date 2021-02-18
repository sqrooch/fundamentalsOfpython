# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: 20м(w) * 5000м(l) * 25кг(d) * 5см(t) = 12500т(m).
# Проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
        self._density = 25
        self._thickness = 5

    def mass_asphalt(self):
        print('Масса асфальта составит',
              round((self._length * self._width * self._density * self._thickness) / 1000, 2), 'тонн')


estimate = Road(input('Введите длину дороги в метрах: '), input('Введите ширину дороги в метрах: '))
estimate.mass_asphalt()
