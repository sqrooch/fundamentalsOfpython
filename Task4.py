# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('Task4.txt', 'r') as Task4, open('Task4_new.txt', 'w') as Task4_new:
    rus_nums = ['Один — ', 'Два — ', 'Три — ', 'Четыре — ']
    nums = Task4.readlines()
    i = 0
    for num in nums:
        num = num.split(' — ')
        num.remove(num[0])
        num.insert(0, rus_nums[i])
        i += 1
        Task4_new.writelines(num)