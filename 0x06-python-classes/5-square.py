#!/usr/bin/python3
"""This module includes modified square class from 4-square"""
BaseSq = __import__("4-square").Square


class Square(BaseSq):
    """ modifed square class that adds additional functionalities"""
    def my_print(self):
        """ prints the square with the right size """
        i = 0
        if (self.__size == 0):
            print("")
        else:
            while (i < self.__size):
                j = 0
                while (j < self.__size):
                    print("#", end="")
                    j += 1
                print("")
                i += 1
