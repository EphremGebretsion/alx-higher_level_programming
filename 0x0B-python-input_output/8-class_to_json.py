#!/usr/bin/python3
"""
onject to dictionary
"""


def class_to_json(obj):
    """returns dictionary of all attributes"""
    return obj.__dict__
