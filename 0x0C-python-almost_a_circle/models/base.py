#!/usr/bin/python3
"""
base class
"""
import csv
import json


class Base:
    """ base class with constructor """
    __nb_objects = 0

    def __init__(self, id=None):
        """ intializing the base class id """
        if not id:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        my_list = []
        if list_objs:
            for i in list_objs:
                my_list.append(i.to_dictionary())
            fname = cls.__name__ + ".json"
            with open(fname, 'w') as my_file:
                my_file.write(cls.to_json_string(my_list))
        else:
            fname = cls.__name__ + ".json"
            with open(fname, "w") as my_file:
                my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = None
        if (cls.__name__ == "Square"):
            dummy = cls(1)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        fname = cls.__name__ + ".json"
        r = []
        try:
            with open(fname, "r") as my_file:
                my_file.seek(0)
                r = cls.from_json_string(my_file.read())
        except FileNotFoundError:
            return []
        i_list = []
        for i in r:
            i_list.append(cls.create(**i))
        return i_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves the objects into csv file"""
        fname = cls.__name__ + ".csv"
        lis = []
        for i in list_objs:
            if cls.__name__ == "Rectangle":
                lis.append([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                lis.append([i.id, i.size, i.x, i.y])
        with open(fname, "w") as my_file:
            my_writer = csv.writer(my_file)
            my_writer.writerows(lis)

    @classmethod
    def load_from_file_csv(cls):
        """loads object datas from a file"""
        fname = cls.__name__ + ".csv"
        lis = []
        with open(fname, 'r') as my_file:
            my_reader = csv.reader(my_file)
            my_file.seek(0)
            for row in my_reader:
                lis.append(row)
        i_list = []
        for i in lis:
            dummy = None
            if (cls.__name__ == "Square"):
                dummy = cls(1)
            elif (cls.__name__ == "Rectangle"):
                dummy = cls(1, 1)
            dummy.id = int(i[0])
            if cls.__name__ == "Square":
                dummy.size = int(i[1])
                dummy.x = int(i[2])
                dummy.y = int(i[3])
            elif cls.__name__ == "Rectangle":
                dummy.width = int(i[1])
                dummy.height = int(i[2])
                dummy.x = int(i[3])
                dummy.y = int(i[4])
            i_list.append(dummy)

        return i_list
