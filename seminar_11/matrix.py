'''Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц'''

class Matrix:
    def __init__(self, matrix: list[list]):
        self._matrix = matrix
        self._rows = len(matrix)
        self._columns = len(matrix[0])

    def __str__(self):
        return "\n".join(str(i) for i in self._matrix)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self._rows == other._rows and self._columns == other._columns:
                list_matrix = []
                for i in range(self._rows):
                    for j in range(self._columns):
                        list_matrix.append(self._matrix[i][j] == other._matrix[i][j])

                return all(list_matrix)
        return False

    def __lt__(self, other):
        if isinstance(other, Matrix):
            if self._rows == other._rows and self._columns == other._columns:
                list_matrix = []
                for i in range(self._rows):
                    for j in range(self._columns):
                        list_matrix.append(self._matrix[i][j] < other._matrix[i][j])

                return all(list_matrix)
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self._rows == other._rows and self._columns == other._columns:
                list_matrix = [[] for i in range(self._rows)]
                for i in range(self._rows):
                    for j in range(self._columns):
                        list_matrix[i].append(self._matrix[i][j] + other._matrix[i][j])
                return Matrix(list_matrix)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self._columns == other._rows:
                list_matrix = [[sum(a * b for a, b in zip(self_row, other_col))
                    for other_col in zip(*other._matrix)]
                        for self_row in self._matrix]
            elif self._rows == other._columns:
                list_matrix = [[sum(a * b for a, b in zip(self_col, other_row))
                    for self_col in zip(*self._matrix)]
                        for other_row in other._matrix]
            return Matrix(list_matrix)
        return False



if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    print(matrix_1)
    print(matrix_3 == matrix_2)
    print(matrix_1 < matrix_2)
    print(matrix_3 > matrix_2)
    print(matrix_3 + matrix_2)
    print('-----------------------')
    print(matrix_3 * matrix_2)

