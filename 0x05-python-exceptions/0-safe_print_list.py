#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            if x and my_list[i]:
                print(my_list[i], end="")
                i += 1
                x -= 1
            else:
                print()
                return i
        except IndexError or x == i:
                print()
                return i
