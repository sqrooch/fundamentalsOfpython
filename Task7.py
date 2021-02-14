# 7. Создать (непрограммно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('Task7.txt', 'r') as Task7, open('Task7.json', 'w') as Task7_new:
    companies = Task7.readlines()

    sum_profit = 0
    sum_positive_profit = 0
    companies_counter = 0
    positive_companies_counter = 0
    profits_dict = {}

    for company in companies:
        company = company.split()
        profit = float(company[2]) - float(company[3])
        print('Прибыль компании', company[0], 'составляет', round(profit, 2), 'руб.')

        if profit >= 0:
            positive_companies_counter += 1
            sum_positive_profit += profit

        profits = [company[0], round(profit, 2)]
        profits_dict.update([profits])

        sum_profit += profit
        companies_counter += 1
    average_profit_dict = dict(average_profit=round(sum_profit / companies_counter, 2))

    print('Средняя прибыль по компаниям с положительной прибылью составляет',
          round(sum_positive_profit / positive_companies_counter, 2), 'руб.\n')

    print([profits_dict, average_profit_dict])
    json.dump([profits_dict, average_profit_dict], Task7_new)
