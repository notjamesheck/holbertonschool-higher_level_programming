#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixx = [i[:] for i in matrix]
    for i in matrixx:
        new_matrix = [[pow(j, 2) for j in i] for i in matrixx]
    return new_matrix
