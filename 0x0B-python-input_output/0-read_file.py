#!/usr/bin/python3
"""this is for reading a file"""


def read_file(filename=""):
    """this function will print the file to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
