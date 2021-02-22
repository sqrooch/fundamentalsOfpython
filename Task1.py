# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        matrix_good_view = f'{self.input_data}'
        matrix_good_view = matrix_good_view.replace('[[', '')
        matrix_good_view = matrix_good_view.replace(']]', '')
        matrix_good_view = matrix_good_view.replace('], [', '\n')
        matrix_good_view = matrix_good_view.replace(',', '')
        return matrix_good_view

    def __add__(self, another):
        i_lines = 0  # счётчик индекса линий в матрице
        if len(self.input_data) <= len(another.input_data):
            for matrix1_line, matrix2_line in zip(self.input_data, another.input_data):
                i = 0  # счётчик индекса элемента в строке
                if len(self.input_data[0]) < len(another.input_data[0]):
                    for el in matrix1_line:
                        matrix2_line.insert(i, el + matrix2_line[i])
                        i += 1
                        matrix2_line.pop(i)
                else:
                    for el in matrix2_line:
                        matrix1_line.insert(i, el + matrix1_line[i])
                        i += 1
                        matrix1_line.pop(i)
                    another.input_data.insert(i_lines, matrix1_line)
                    i_lines += 1
                    another.input_data.pop(i_lines)
                    if len(self.input_data) < len(another.input_data)\
                            and len(self.input_data[-1]) > len(another.input_data[-1]):
                        for matrix2_line in another.input_data[-(len(another.input_data) - len(self.input_data)):]:
                            for _ in range(len(self.input_data[-1]) - len(another.input_data[-1])):
                                matrix2_line.append(0)
            return another.__str__()
        else:
            for matrix1_line, matrix2_line in zip(self.input_data, another.input_data):
                i = 0  # счётчик индекса элемента в строке
                if len(self.input_data[0]) <= len(another.input_data[0]):
                    for el in matrix1_line:
                        matrix2_line.insert(i, el + matrix2_line[i])
                        i += 1
                        matrix2_line.pop(i)
                    self.input_data.insert(i_lines, matrix2_line)
                    i_lines += 1
                    self.input_data.pop(i_lines)
                    if len(self.input_data) > len(another.input_data) and len(self.input_data[-1]) < len(
                            another.input_data[-1]):
                        for matrix1_line in self.input_data[-(len(self.input_data) - len(another.input_data)):]:
                            for _ in range(len(another.input_data[-1]) - len(self.input_data[-1])):
                                matrix1_line.append(0)
                else:
                    for el in matrix2_line:
                        matrix1_line.insert(i, el + matrix1_line[i])
                        i += 1
                        matrix1_line.pop(i)
            return self.__str__()


matrix1 = Matrix([[1, 1, 1, 1], [0, 1, 1, 1]])
matrix2 = Matrix([[0, 1, 0], [1, 0, 1], [1, 1, 3], [1, 1, 1], [3, 1, 1]])
print(matrix1.__add__(matrix2))
