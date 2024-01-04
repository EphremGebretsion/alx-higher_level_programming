#!/usr/bin/python3
"""this module have rectangle class with setter and getters"""


class Rectangle:
    """Rectangle class with getter and seters"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if (self.width == 0 or self.height == 0):
            return ""
        rec_image = ((str(self.print_symbol) * self.width) + "\n") * (
                     self.height - 1)
        return rec_image + (str(self.print_symbol) * self.width)

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.width * rect_1.height) >= (rect_2.width * rect_2.height):
            return rect_1
        else:
            return rect_2
