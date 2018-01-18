#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            h = f.read()
            print(h, end="")
        else:
            while nb_lines > 0:
                h = f.readline()
                print(h, end="")
                nb_lines -= 1
