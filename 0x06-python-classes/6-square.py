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
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        x, y = self
        print("x = {}, y = {}".format(x, y)

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) != int:
                raise TypeError("position must be a tuple pf 2 positive integers")
            if i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value    
           
        
