#!/usr/bin/python3
""" student class """


class Student():
    """ student class with json dictionary convertor """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (not attrs):
            return (self.__dict__)
        if (type(attrs) != list):
            return (self.__dict__)
        if (len(attrs) == 0):
            return (self.__dict__)
        newlist = {}
        dic = self.__dict__
        for i in attrs:
            if (i in dic):
                newlist[i] = dic[i]
        return (newlist)
