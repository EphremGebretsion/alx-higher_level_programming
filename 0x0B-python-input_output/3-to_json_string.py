#!/usr/bin/python3
"""convert to JSON"""


import json


def to_json_string(my_obj):
    """ return the JSON representation of my_obj"""
    return (json.dumps(my_obj))
