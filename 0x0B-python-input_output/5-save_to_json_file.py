#!/usr/bin/python3
"""writes to jason file using JSON representation"""


import json
def save_to_json_file(my_obj, filename):
    json.dump(my_obj, filename)
