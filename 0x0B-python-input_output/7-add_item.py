#!/usr/bin/python3
"""
adding the provided arguments to a list
in a file
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []
with open("add_item.json", mode="a+", encoding="UTF8") as my_file:
    my_file.seek(0)
    if my_file.read():
        my_list = load_from_json_file("add_item.json")

i = 1
while i < len(argv):
    my_list.append(argv[i])
    i += 1
save_to_json_file(my_list, "add_item.json")
