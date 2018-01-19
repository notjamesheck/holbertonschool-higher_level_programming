#!/usr/bin/python3


def number_of_lines(filename=""):
    l = 0
    with open(filename, 'r') as f:
        while f.readline():
            l += 1
    return l
