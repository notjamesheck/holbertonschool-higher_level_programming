#!/usr/bin/python3
"""Module that defines a rectangle
"""


class Rectangle:
    """Class that defines a rectangle
    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        for i in range(self.height):
            for h in range(self.width):
                print(self.print_symbol, end="")
            if i + 1 < self.height:
                print()

        return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances is not 0:
            Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
