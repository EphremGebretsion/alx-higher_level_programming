#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {elem: a_dictionary[elem] * 2 for elem in list(a_dictionary)}
