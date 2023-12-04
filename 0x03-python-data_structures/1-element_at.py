#!/usr/bin/python3
def element_at(my_list, idx):
    if (not my_list) or idx < 0:
        return None
    if len(my_list) <= idx:
        return None
    return my_list[idx]
