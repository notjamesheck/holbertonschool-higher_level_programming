#!/usr/bin/python3


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        else:
            return self.__dict__
