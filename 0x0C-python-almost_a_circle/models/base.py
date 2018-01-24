#!/usr/bin/python3
import json
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

    def to_json_string(list_dictionaries):

        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
    
