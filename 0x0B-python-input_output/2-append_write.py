#!/usr/bin/python3
"""append test to a file"""


def append_write(filename="", text=""):
    """this will append a test to the file: filename"""
    with open(filename, mode='a', encoding="utf-8") as my_file:
        return (my_file.write(text))
