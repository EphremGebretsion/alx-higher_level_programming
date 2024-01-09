#!/usr/bin/python3
"""
class with json representation
"""


class Student:
    """
    student class with full name, age and json representation method
    """
    def __init__(self, first_name, last_name, age):
        """initialising method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary to encode in json"""
        return self.__dict__
