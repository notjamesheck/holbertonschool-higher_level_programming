#!/bin/usr/python3
from add_0 import add


def add(a, b):
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
