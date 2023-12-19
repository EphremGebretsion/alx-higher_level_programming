#!/usr/bin/python3
""" this module includes the square class
that hase been modified with more added features
"""


class Square:
    """creating a square class with error exceptions,
    constructors"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor for the class
        that sets the nesesery values to its elements"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (type(position) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2 or type(position[0]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """ calculates the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """ returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value the square size to the gived value"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints the square with the exact size and
        positions the square with the position value"""
        if (self.__size == 0):
            print("")
        else:
            i = 0
            if (self.__position[1] > 0):
                p = 0
                while (self.__position[1] > p):
                    print("")
                    p += 1
            while(i < self.__size):
                j = 0
                po = " " * self.__position[0]
                print(po, end="")
                while(j < self.__size):
                    print("#", end="")
                    j += 1
                print("")
                i += 1

    @property
    def position(self):
        """ gets the position value of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the position of the square to the given value"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
