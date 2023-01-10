#!/usr/bin/python3
"""writes to jason file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes my_obj to a file filename using JSON"""
    json.dump(my_obj, filename)
