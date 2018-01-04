#!/usr/bin/python3
"""
class square that defines a square
example of docstring on the __init__ method
Args:
    size (int): private instance attribute
"""


class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        message = "position must be a tuple of 3 positive integers"
        if len(value) != 2 or type(value) != tuple:
            raise TypeError(message)
        for i in value:
            if type(i) != int:
                raise TypeError(message)
            if i < 0:
                raise TypeError(message)
        self.__position = value
