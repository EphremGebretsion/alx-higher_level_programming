#!/usr/bin/python3
""" square class """


class Square:
    """creating a square class with error exceptions"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor for the class"""
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
        """ calculates the area """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints the square """
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
        """ gets the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the position """
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
