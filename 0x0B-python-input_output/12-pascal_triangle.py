#!/usr/bin/python3
"""
pascal's triangle challenge
"""


def pascal_triangle(n):
    """returns a two dimentional pascal triagle list of integers"""
    res = []
    if n <= 0:
        return res
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(res[i - 1][j - 1] + res[i - 1][j])
        res.append(tmp[:])
    return res
