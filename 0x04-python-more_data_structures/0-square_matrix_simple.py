#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    an_matrix = matrix.copy()
    for m in range(len(matrix)):
        an_matrix[m] = list(map(lambda x: x**2, matrix[m]))
        return (an_matrix)
