#!/usr/bin/python3
"""Module that prints my name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints my name
    """
    name = ""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    name += first_name + " "
    if len(last_name) != 0:
        name += last_name

    print("My name is " + name)
