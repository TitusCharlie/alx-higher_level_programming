#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    result = []
    for row in range(len(matrix)-1):
        row_1 = []
        for col in matrix:
            row_1.append(col)
        result.append(row_1)
    print(result)
