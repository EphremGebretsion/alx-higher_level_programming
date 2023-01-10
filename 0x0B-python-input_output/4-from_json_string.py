#!/usr/bin/python3
""" JSON to python data structure"""


import json
def from_json_string(my_str):
    """returns the original python data structure from json object"""
    return (json.loads(my_str))
