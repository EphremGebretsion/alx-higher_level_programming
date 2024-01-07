#!/usr/bin/pyhton3
"""
this script prints a given test
and also adds indentation for some selected characters
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    n = 1
    for c in text:
        if n and c == " ":
            continue
        print(c, end="")
        if c in [".", "?", ":"]:
            print("\n")
            n = 1
        else:
            n = 0
