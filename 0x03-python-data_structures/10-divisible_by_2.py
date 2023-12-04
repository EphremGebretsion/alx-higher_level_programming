#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    return [True if not i % 2 else False for i in my_list]
