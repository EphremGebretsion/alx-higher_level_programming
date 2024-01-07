#!usr/bin/python3
"""
prints the name
using say my name function it will repeat the name
"""


def say_my_name(first_name, last_name=""):
    """
    prints the full name
    if there is no last name it prints the first name only
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {fn} {ln}".format(fn=first_name, ln=last_name))
