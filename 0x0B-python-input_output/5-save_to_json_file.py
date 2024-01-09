#!/usr/bin/python3
"""
json encoding to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ecodes the object to the file"""
    with open(filename, mode="w", encoding="UTF8") as my_file:
        json.dump(my_obj, my_file)
