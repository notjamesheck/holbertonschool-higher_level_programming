#!/usr/bin/python3


class BaseGeometry():

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width=0, height=0):

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)


class Square(Rectangle):

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
