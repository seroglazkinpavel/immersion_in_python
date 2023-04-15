# Напишите функцию для транспонирования матрицы

matrix = [[5, 4, 3],
          [2, 4, 6],
          [4, 7, 9],
          [8, 1, 3]
          ]


def func_matrix(matrix: list[list[int]]) -> list:
    """Определяем пустую матрицу обратного порядка"""
    trans_result = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                    ]
    for row in range(len(matrix)):
        for element in range(len(matrix[0])):
            trans_result[element][row] = matrix[row][element]
    print("Транспонирование матрицы matrix равно: ")
    for res in trans_result:
        print(res)


func_matrix(matrix)
