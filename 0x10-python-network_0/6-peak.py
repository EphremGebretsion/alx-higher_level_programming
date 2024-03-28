#!/usr/bin/python3
"""finds the peak of numbers"""


def find_peak(list_of_integers):
    """returns the peack of list_of_integers"""
    if not list_of_integers:
        return None
    if len(list_of_integers) < 2:
        return list_of_integers[0]
    peak = None
    last = len(list_of_integers) - 1
    if list_of_integers[0] > list_of_integers[1]:
        peak = list_of_integers[0]
    i = 1
    while i < last:
        left = list_of_integers[i - 1]
        right = list_of_integers[i + 1]
        current = list_of_integers[i]
        if current > left and current > right:
            return current
        if current == left and current == right:
            if peak is not None:
                return peak
            else:
                return current
        i += 1
    if list_of_integers[-1] > list_of_integers[-2]:
        peak = list_of_integers[-1]
    return peak
