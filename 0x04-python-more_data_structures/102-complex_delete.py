#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_del = []
    poped = {}
    for i in a_dictionary:
        if (a_dictionary[i] == value):
            keys_del.append(i)
    for k in keys_del:
        a_dictionary.pop(k)
    return a_dictionary
