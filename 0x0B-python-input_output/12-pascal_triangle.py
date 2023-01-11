#!/usr/bin/python3
""" pascal triangle """


def pascal_next(prev_list):
    """create the next level of pasical layer"""
    ma = len(prev_list) - 1
    new_list = []
    for i in range(ma):
        new_list.append(prev_list[i] + prev_list[i + 1])
    new_list.append(1)
    new_list.insert(0, 1)
    return (new_list)


def pascal_triangle(n):
    """creates a pasical triangle list"""
    if (n < 1):
        return ([])
    pascal_list = []
    for i in range(1, (n + 1)):
        if (i == 1):
            pascal_list.append([1])
        if(i == 2):
            pascal_list.append([1, 1])
        if (i > 2):
            pascal_list.append(pascal_next(pascal_list[i - 2]))
    return (pascal_list)
