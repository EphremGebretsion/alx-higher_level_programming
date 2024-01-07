#!/usr/bin/python3
"""
matrix division  module
this module includes the function to devide matrix
"""


def matrix_divided(matrix, div):
    """
    divies the given matrix by div
    and throughs error if something went wrong
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(messge)
    if not len(matrix):
        raise TypeError(message)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for m in matrix:
        if type(m) is not list:
            raise TypeError(message)
        if (len(matrix[0]) != len(m)):
            raise TypeError("Each row of the matrix must have the same size")
        for n in m:
            if type(n) not in [int, float]:
                raise TypeError(message)
    res = []
    for m in matrix:
        tmp = []
        for n in m:
            tmp.append(round((n / div), 2))
        res.append(tmp)
    return res
