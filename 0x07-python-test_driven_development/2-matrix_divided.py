#!/usr/bin/python3
"""Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(len(matrix)):
        for h in matrix[i]:
            if type(h) != int and type(h) != float:
                raise TypeError(message)
    ml = 0
    for i in range(len(matrix)):
        if i == 0:
            ml = len(matrix[i])
        if len(matrix[i]) != ml:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    nl = []
    for i in range(len(matrix)):
        it = []
        for h in matrix[i]:
            try:
                it.append(round(h/div, 2))
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
        nl.append(it)
    return nl
