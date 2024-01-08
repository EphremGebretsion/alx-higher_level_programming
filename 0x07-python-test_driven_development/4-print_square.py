#!/usr/bin/python3
"""
this script will print a square
the square size will dipend on the size parameter
"""


def print_square(size):
    """
    pints a square of # character
    size: is the size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        j = 0
        while (j < size):
            print("#", end="")
            j += 1
        i += 1
        print("")
