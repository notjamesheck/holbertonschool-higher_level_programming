#!/usr/bin/python3
def multiply_by_2(my_dict):
    d = dict(my_dict)
    for key in d:
        d[key] *= 2
    return d
