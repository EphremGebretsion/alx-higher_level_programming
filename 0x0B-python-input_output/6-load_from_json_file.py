#!/usr/bin/python3
"""create object form JSON file"""


import json


def load_from_json_file(filename):
    """retirns the python object structure from json file"""
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return (json.load(my_file))
