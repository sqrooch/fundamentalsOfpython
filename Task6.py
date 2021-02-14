# 6. Необходимо создать (непрограммно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('Task6.txt', 'r') as Task6:
    schedule = Task6.readlines()
    schedule_dict = {}
    for subject in schedule:
        subject = subject.split(':')
        subject = [subject[0], subject[1].replace('\n', '')]
        subject = [subject[0], subject[1].replace(' —', '')]
        subject = [subject[0], subject[1].replace('.', '')]
        subject = [subject[0], subject[1].replace('(л)', '')]
        subject = [subject[0], subject[1].replace('(пр)', '')]
        subject = [subject[0], subject[1].replace('(лаб)', '')]
        subject = [subject[0], subject[1].split()]
        sum_hours = 0
        for hours in subject[1]:
            hours = int(hours)
            sum_hours += hours
        subject = [subject[0], sum_hours]
        schedule_dict.update([subject])
    print(schedule_dict)