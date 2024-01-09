#!/usr/bin/python3
"""
writing to a file
"""


def write_file(filename="", text=""):
    """writes text to a file"""
    with open(filename, mode="w", encoding="UTF8") as my_file:
        return my_file.write(text)
