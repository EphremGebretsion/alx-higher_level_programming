#!/usr/bin/python3
""" reload student from json object"""


class Student():
    """ student class with json dictionary convertor and reloader"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return (self.__dict__)
        if (type(attrs) != list):
            return (self.__dict__)

        newlist = {}
        dic = self.__dict__
        for i in attrs:
            if (i in dic):
                newlist[i] = dic[i]
        return (newlist)

    def reload_from_json(self, json):
        if ("first_name" in json):
            self.first_name = json["first_name"]
        if ("last_name" in json):
            self.last_name = json["last_name"]
        if ("age" in json):
            self.age = json["age"]
