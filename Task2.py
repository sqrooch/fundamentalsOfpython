# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('Task2.txt', 'r') as Task2:
    strs_in_text = Task2.readlines()
    print('\nВ тексте', len(strs_in_text), 'строк:\n')
    for str_line in strs_in_text:
        str_line = str_line.replace('\n', '')
        print('Количество символов в строке "', str_line, '" =', len(str_line))

# При условии, что пробел тоже считается символом.
# В противном случае добавить метод .replace(' ', '') в цикл.
