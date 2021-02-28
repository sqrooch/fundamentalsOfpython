# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

month_dict = {'январь': 1,
              'февраль': 2,
              'март': 3,
              'апрель': 4,
              'май': 5,
              'июнь': 6,
              'июль': 7,
              'август': 8,
              'сентябрь': 9,
              'октябрь': 10,
              'ноябрь': 11,
              'декабрь': 12}


class Date:
    def __init__(self, date_as_words):
        self.date_as_words = date_as_words

    @classmethod
    def transform_date_in_nums(cls, date_as_words):
        is_true_month_name = 'miss'
        cls.date_as_words = date_as_words.split('-')
        for key in month_dict.keys():
            if key == month:
                is_true_month_name = 'hit'
        if is_true_month_name == 'hit':
            cls.date_as_words.insert(1, month_dict.get(cls.date_as_words[1]))
            cls.date_as_words.pop(2)
        else:
            print('Неправильный ввод. Попробуйте ещё раз.')
            exit(0)
        if cls.date_as_words[0].isdigit() and cls.date_as_words[2].isdigit():
            pass
        else:
            print('Число и месяц должны быть написаны цифрами. Попробуйте ещё раз.')
            exit(0)

        i = 1
        for el in cls.date_as_words:
            el = int(el)
            cls.date_as_words.insert(0, el)
            cls.date_as_words.pop(i)
            i += 1
        cls.date_as_words.reverse()
        return cls.date_as_words

    @staticmethod
    def validator(date_as_words):
        validated_result = Date.transform_date_in_nums(date_as_words)
        if validated_result[2] % 4 == 0 \
                and validated_result[1] == 2 \
                and (validated_result[0] > 29
                     or validated_result[0] < 1):
            print('В високосный год в феврале 29 дней. Попробуйте ещё раз.')
        elif validated_result[2] % 4 != 0 \
                and validated_result[1] == 2 \
                and (validated_result[0] > 28
                     or validated_result[0] < 1):
            print('В феврале 28 дней. Попробуйте ещё раз.')
        elif (validated_result[1] == 4
              or validated_result[1] == 6
              or validated_result[1] == 9
              or validated_result[1] == 11) \
                and (validated_result[0] > 30
                     or validated_result[0] < 1):
            print('В этом месяце 30 дней. Попробуйте ещё раз.')
        elif validated_result[0] > 31 or validated_result[0] < 1:
            print('В месяце 31 день. Попробуйте ещё раз.')
        else:
            i = 1
            for el in validated_result:
                if el < 10:
                    el = '0' + str(el)
                else:
                    el = str(el)
                validated_result.insert(0, el)
                validated_result.pop(i)
                i += 1
            validated_result.reverse()
            print('.'.join(validated_result))


number = input('Введите число (цифрами): ')
month = input('Введите месяц (буквенно в Им.падеже): ').lower()
year = input('Введите год (цифрами): ')
Date.validator(f'{number}-{month}-{year}')
# Я намеренно не ставил валидность на года,
# потому что считаю, что года могут быть любые, даже отрицательные (до нашей эры например).
