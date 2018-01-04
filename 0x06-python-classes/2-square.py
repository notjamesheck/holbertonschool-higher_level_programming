#!/usr/bin/python3
"""
class square that defines a square
example of docstring on the __init__ method
Args:
    size (int): private instance attribute
"""


class Square():
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
