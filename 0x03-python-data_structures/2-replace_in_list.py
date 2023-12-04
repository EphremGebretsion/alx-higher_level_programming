#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (not my_list) or idx < 0:
        return my_list
    if len(my_list) <= idx:
        return my_list

    my_list[idx] = element

    return my_list
