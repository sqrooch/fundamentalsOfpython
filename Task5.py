# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce().
from functools import reduce


def multi(previous_result, next_element):
    return previous_result * next_element


print(reduce(multi, [num for num in range(100, 1001, 2)]))
