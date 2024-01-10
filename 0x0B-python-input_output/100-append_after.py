#!/usr/bin/python3
"""
peending inbetween a text file
"""


def append_after(filename="", search_string="", new_string=""):
    rd = []
    res = []
    with open(filename, mode="r", encoding="UTF8") as my_file:
        my_file.seek(0)
        rd = my_file.readlines()
    for line in rd:
        res.append(line)
        if search_string in line:
            res.append(new_string)
    with open(filename, mode="w", encoding="UTF8") as my_file:
        my_file.write(''.join(res))
