#!/usr/bin/python3
"""write to the file"""


def write_file(filename="", text=""):
    """writes the text to the file filename"""
    with open(filename, mode='w', encoding="utf-8") as my_file:
        num = my_file.write(text)
    return (num)
