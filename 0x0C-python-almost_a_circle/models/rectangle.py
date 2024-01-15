#!/usr/bin/python3
"""
making rectangle subclass from base
"""
from models.base import Base


class Rectangle(Base):
    """rectangle subclass of base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, w):
        """ width setter"""
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, h):
        """height setter"""
        if type(h) is not int:
            raise TypeError("hight must be an integer")
        if h <= 0:
            raise ValueError("hight must be > 0")
        else:
            self.__height = h

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, val):
        """x setter"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, val):
        """y setter"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """calculates and returns the area"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle to stdout"""
        p = ""
        if self.__x < 0:
            p = ("#" * self.__width) + (" " * abs(self.__x))
        else:
            p = (" " * self.__x) + ("#" * self.__width)
        if (self.__y > 0):
            j = "\n" * self.__y
            print(j, end="")
        for h in range(self.__height):
            print(p)
        if (self.__y < 0):
            j = "\n" * abs(self.__y)
            print(j, end="")

    def __str__(self):
        """tring representation of the rectangle class"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """updates the elements of the class using
        the args array"""
        attrs = ("id", "width", "height", "x", "y")
        i = 0
        for v in args:
            setattr(self, attrs[i], v)
            i += 1
        if not args:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """returns the dictionary representation of the class"""
        d = {'x': self.__x, 'y': self.__y, 'id': self.id}
        d["height"] = self.__height
        d["width"] = self.__width
        return d
