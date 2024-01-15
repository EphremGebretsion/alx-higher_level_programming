#!/usr/bin/python3
"""
square class
that is inherited from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square subclass that is inherited from rectangle
    class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """gets the size of the square"""
        return self.width

    @size.setter
    def size(self, val):
        """sets the size of the square"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """updates the attributes of the square class"""
        attrs = ("id", "size", "x", "y")
        i = 0
        for v in args:
            setattr(self, attrs[i], v)
            i += 1

        if not args:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """returns the dictionary representation of the class"""
        d = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return d
