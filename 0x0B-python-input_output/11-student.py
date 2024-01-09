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
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """returns a dictionary to encode in json"""
        res = self.__dict__
        if not attrs:
            return res
        else:
            if (type(attrs) is list):
                for k in attrs:
                    if type(k) is not str:
                        return res
                res = {}
                for k in self.__dict__:
                    if k in attrs:
                        res[k] = self.__dict__[k]
        return res

    def reload_from_json(self, json):
        """replace all attributes of Student"""
        for k in json:
            setattr(self, k, json[k])
