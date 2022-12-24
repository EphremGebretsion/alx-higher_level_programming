#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    er = "Exception: Unkown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        print(er, file=sys.stderr)
        return (False)
