#!/usr/bin/python3
"""
reads a file and prints to stdout
"""


def read_file(filename=""):
    """
    reads a file and prints its content of stdout
    """
    with open(filename, mode="r", encoding="UTF8") as my_file:
        for line in my_file:
            print(line, end="")
