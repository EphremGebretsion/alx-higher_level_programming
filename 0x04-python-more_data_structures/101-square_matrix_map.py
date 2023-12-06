#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    res = []
    for ar in matrix:
        res.append([i ** 2 for i in ar])
    return res
