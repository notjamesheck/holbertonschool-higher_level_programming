#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, 'r') as f:
        h = f.read()
        for line in h:
            print(line, end="")
