# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('Task3.txt', 'r') as Task3:
    salary_list = Task3.readlines()
    print('\nМенее 20 тыс.руб. получают:')
    average_salary = 0
    for position in salary_list:
        position = position.replace('\n', '')
        position = position.replace(' ', '')
        position = position.replace('руб.', '')
        position = position.split('-')
        if float(position[1]) < 20000:
            print(position[0])
        average_salary += float(position[1]) / len(salary_list)
    print('\nСредний оклад сотрудника =', round(average_salary, 2), 'руб.')