#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (not my_list) or idx < 0:
        return my_list
    if len(my_list) <= idx:
        return my_list

    new_list = my_list[:]
    new_list[idx] = element

    return new_list

