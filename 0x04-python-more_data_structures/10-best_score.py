#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return None
    keys = list(a_dictionary)
    best = keys[0]
    for elem in keys:
        if (a_dictionary[best] < a_dictionary[elem]):
            best = elem
    return best
