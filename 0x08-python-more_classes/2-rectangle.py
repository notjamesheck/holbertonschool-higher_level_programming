#!/usr/bin/python3
"""Module that defines a rectangle
"""


class Rectangle:
    """Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        # width must be integer (use isinstance),
        # else raise TypeError("width must be an integer")
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        # if width < 0, raise ValueError("width must be >= 0")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        # height must be integer (use isinstance),
        # else raise TypeError("height must be an integer")
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        # if height < 0, raise ValueError("height must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
