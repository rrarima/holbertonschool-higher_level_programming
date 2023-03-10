#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function taht devides all elemens of a matrix"""

    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_2 = "Each row of the matrix must have the same size"
    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(msg_2)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(msg_1)
            else:
                inner_list.append(round(items / div, 2))
        new_matrix.append(inner_list)

    return new_matrix
