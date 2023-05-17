#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return new_matrix
    new_matrix = [[m*m for m in k] for k in matrix]
    return new_matrix
