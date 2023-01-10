#!/usr/bin/python3
import json
"""writes to jason file using JSON representation"""


def save_to_json_file(my_obj, filename):
    """writes my_obj to a file filename using JSON"""
    with open(filename, mode='r', encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
