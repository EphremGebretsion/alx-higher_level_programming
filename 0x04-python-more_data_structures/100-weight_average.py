#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list) or my_list is None:
        return 0
    num = 0
    den = 0
    for i in my_list:
        num += i[0] * i[1]
        den += i[1]
    return num / den
