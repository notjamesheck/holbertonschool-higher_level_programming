#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    c = a[0] + b[0]
    d = a[1] + b[1]
    return (c, d)
