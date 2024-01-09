#!/usr/bin/python3
"""
decoding form a json file
"""
import json


def load_from_json_file(filename):
    """returns the decoded string from the file"""
    with open(filename, mode="r", encoding="UTF8") as my_file:
        return json.load(my_file)
