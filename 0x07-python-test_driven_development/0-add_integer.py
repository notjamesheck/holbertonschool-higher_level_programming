#!/usr/bin/python3
"""a function that adds two integers
"""


def add_integer(a, b):
    """checks type, corrects value to int
    """
    if type(a) == float:
        a = int(a)
    """raises error if operation not possible
    """
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    if type(b) != int:
        raise TypeError("b must be an integer")
    """returns added values
    """
    return a + b
