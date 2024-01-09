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

    def to_json(self, attrs=None):
        """returns a dictionary to encode in json"""
        res = self.__dict__
        if not attrs:
            return res
        else:
            if (type(attrs) is list):
                res = {}
                for k in attrs:
                    if k in self.__dict__:
                        res[k] = self.__dict__[k]
        return res
