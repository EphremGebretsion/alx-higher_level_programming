#!/usr/bin/python3
"""
ineriting and adding additional functionality for
list class
"""


class MyList(list):
    """
    subclass for list
    """
    def print_sorted(self):
        """ prints sorted new list"""
        j = self[:]
        j.sort()
        print(j)
