#!/usr/bin/python3
""" square class """


class Square:
    """creating a square class with error exceptions"""
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        i = 0
        if (self.__size == 0):
            print("")
        else:
            while(i < self.__size):
                j = 0
                while(j < self.__size):
                    print("#", end="")
                    j += 1
                print("")
                i += 1
