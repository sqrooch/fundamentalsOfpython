# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""В условии задачи не сказано использовать функцию complex() и нет разрешения подключать дополнительные библиотеки,
поэтому решил задачу без дополнительных инструментов. В любом случае, уверяю, что я про них знаю, умею ими пользоваться
и намеренно пошёл по сложному пути. Из принципа..."""


def valid():
    while True:
        user_input = input('Введите комплексное число, включающее префикс"i": ')
        find_bad_el = ''
        for el in user_input[:-1]:
            if '+-0123456789'.find(el) == -1:
                find_bad_el = 'hit'  # в строке неприемлемый элемент.
        if user_input[-1] != 'i' \
                or user_input[0] == '+' \
                or user_input[0] == '0' \
                or user_input.count('+') > 1 \
                or user_input.count('-') > 2 \
                or user_input.find('--') != -1 \
                or user_input.find('-0') != -1 \
                or user_input.find('+0') != -1 \
                or user_input.find('+1i') != -1 \
                or user_input.find('-1i') != -1 \
                or (user_input.find('+') == -1 and user_input.find('-') == -1 and user_input[0] == '0') \
                or find_bad_el == 'hit':
            print('Ошибка при вводе комплексного числа! Попробуйте ещё.')
        else:
            return user_input


class C_nums:
    def __init__(self, cplx_num):
        self.cplx_num = cplx_num
        self.real = 0
        self.im = 0
        if len(self.cplx_num) == 1:
            self.im = 1
        elif len(self.cplx_num) == 2 and self.cplx_num.find('-') != -1:
            self.im = -1
        elif self.cplx_num.find('+') == -1 and self.cplx_num.find('-') == -1:
            self.im = self.cplx_num[:-1]
        elif self.cplx_num.find('+') != -1:
            self.real = self.cplx_num.split('+')[0]
            if len(self.cplx_num.split('+')[1]) == 1:
                self.im = 1
            else:
                self.im = self.cplx_num.split('+')[1][:-1]
        else:
            self.cplx_num = self.cplx_num[::-1]
            self.real = self.cplx_num[self.cplx_num.index('-') + 1:]
            if len(self.real[::-1]) == 0:
                self.real = 0
            else:
                self.real = self.real[::-1]
            self.im = self.cplx_num[1:self.cplx_num.index('-') + 1]
            if self.im[::-1] == '-':
                self.im = -1
            else:
                self.im = self.im[::-1]
        self.real = int(self.real)
        self.im = int(self.im)

    def __add__(self, other):
        other.real = int(other.real)
        other.im = int(other.im)

        print('Сложим два этих комплексных числа:')
        if self.real + other.real != 0 and self.im + other.im > 1:
            print(f'Получим: {self.real + other.real}+{self.im + other.im}i')
        elif self.real + other.real != 0 and self.im + other.im == 1:
            print(f'Получим: {self.real + other.real}+i')
        elif self.real + other.real == 0 and self.im + other.im > 1:
            print(f'Получим: {self.im + other.im}i')
        elif self.real + other.real == 0 and self.im + other.im == 1:
            print(f'Получим: i')
        elif self.real + other.real != 0 and self.im + other.im < -1:
            print(f'Получим: {self.real + other.real}{self.im + other.im}i')
        elif self.real + other.real != 0 and self.im + other.im == -1:
            print(f'Получим: {self.real + other.real}-i')
        elif self.real + other.real == 0 and self.im + other.im < -1:
            print(f'Получим: {self.im + other.im}i')
        elif self.real + other.real == 0 and self.im + other.im == -1:
            print(f'Получим: -i')
        else:
            print(f'Получим: {self.real + other.real}')

    def __mul__(self, other):
        other.real = int(other.real)
        other.im = int(other.im)

        print('Перемножим два этих комплексных числа:')
        if self.real * other.real - self.im * other.im != 0 and self.real * other.im + self.im * other.real > 1:
            print(f'Получим: {self.real * other.real - self.im * other.im}'
                  f'+{self.real * other.im + self.im * other.real}i')
        elif self.real * other.real - self.im * other.im != 0 and self.real * other.im + self.im * other.real == 1:
            print(f'Получим: {self.real * other.real - self.im * other.im}+i')
        elif self.real * other.real - self.im * other.im == 0 and self.real * other.im + self.im * other.real > 1:
            print(f'Получим: {self.real * other.im + self.im * other.real}i')
        elif self.real * other.real - self.im * other.im == 0 and self.real * other.im + self.im * other.real == 1:
            print(f'Получим: i')
        elif self.real * other.real - self.im * other.im != 0 and self.real * other.im + self.im * other.real < -1:
            print(f'Получим: {self.real * other.real - self.im * other.im}'
                  f'{self.real * other.im + self.im * other.real}i')
        elif self.real * other.real - self.im * other.im != 0 and self.real * other.im + self.im * other.real == -1:
            print(f'Получим: {self.real * other.real - self.im * other.im}-i')
        elif self.real * other.real - self.im * other.im == 0 and self.real * other.im + self.im * other.real < -1:
            print(f'Получим: {self.real * other.im + self.im * other.real}i')
        elif self.real * other.real - self.im * other.im == 0 and self.real * other.im + self.im * other.real == -1:
            print(f'Получим: -i')
        else:
            print(f'Получим: {self.real * other.real - self.im * other.im}')


c_num1 = C_nums(valid())
c_num2 = C_nums(valid())
c_num1 + c_num2
c_num1 * c_num2
