# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Task5.txt', 'w') as Task5:
    get_nums = 'abc'
    while not get_nums == '':
        get_nums = input('Дополните ряд числом (для окончания ввода введите пустую строку): ')
        Task5.write(get_nums+' ')

with open('Task5.txt', 'r') as Task5:
    nums = Task5.read().split(' ')
    nums_sum = 0
    for num in nums[:-2]:
        num = float(num)
        nums_sum += num
    print('\nСумма чисел =', round(nums_sum, 2))