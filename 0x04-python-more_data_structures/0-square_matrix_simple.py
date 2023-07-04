#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mul_result = []
    for row in matrix:
        result = []
       [result.append(row[col]**2 for col in range(3))]
      #  for col in range(3):
       #     result.append(row[col]**2)
        mul_result.append(result)
    return mul_result
