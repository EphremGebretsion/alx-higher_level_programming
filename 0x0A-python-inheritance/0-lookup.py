#!/usr/bin/python3
"""
this script includes a function for lookup for all
attributes and method objects in a class
"""


def lookup(obj):
    """ 
    looks for all attributes and methods
    and returns them
    """
    return dir(obj)
