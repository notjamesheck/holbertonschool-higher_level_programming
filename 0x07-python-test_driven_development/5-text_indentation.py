#!/usr/bin/python3
"""Module that prints a text with 2 new lines after delims(:?,)
"""


def text_indentation(text):
    """Function that prints a text w/ 2 new lines after delims(:?,)
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(". ", ".\n\n")
    print(text), print()
