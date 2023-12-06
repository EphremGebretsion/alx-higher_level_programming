#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for elem in set(my_list):
        sum += elem
    return sum
