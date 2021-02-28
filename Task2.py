# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class Zero(Exception):
    def __init__(self, notice):
        self.notice = notice


while True:
    try:
        dividend = float(input('Введите делимое: '))
        break
    except ValueError:
        print('Вы ввели не число.\n')

while True:
    try:
        divider = float(input('Введите делитель: '))
        if divider == 0:
            raise Zero('Деление на ноль запрещено!\n')
    except ValueError:
        print('Вы ввели не число.\n')
    except Zero as err:
        print(err)
    else:
        print('\nВсё в порядке. Ответ:', round(dividend / divider, 2))
        break
