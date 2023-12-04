#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    new_string = my_string[:]
    i = 0
    while i < len(new_string):
        if (new_string[i] in ["C", "c"]):
            new_string = new_string[:i] + new_string[i + 1:]
        i += 1
    return new_string
