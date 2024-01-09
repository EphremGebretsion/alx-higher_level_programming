#!/usr/bin/python3
"""
appending a text to a file
"""


def append_write(filename="", text=""):
    """appends text to the file"""
    with open(filename, mode="a", encoding="UTF8") as my_file:
        return my_file.write(text)
