#!/usr/bin/python3
"""the first class Base
"""


class Base():
    """define class, non-base counter
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """init self and id
        """
        if id is not None:
            """value of base object
            """
            self.id = id
        else:
            """count num of non-base objects
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
