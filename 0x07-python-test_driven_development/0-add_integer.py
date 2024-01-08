#!/usr/bin/python3
"""
addition calcularing module
checks the type of the parameters before
calculating the result
"""


def add_integer(a, b=98):
    """
    addition function
    """
    if not a:
        raise TypeError("a must be an integer")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
