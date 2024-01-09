#!/usr/bin/python3
"""
json decoding
"""
import json


def from_json_string(my_str):
    """returns the json decoding of the object"""
    return json.loads(my_str)
