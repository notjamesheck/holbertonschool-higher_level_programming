#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while True:
        try:
            print("{:d}".format(my_list[i]), end="") 
            i += 1
            print("What is i? {:d}".format(i))
        except ValueError:
            return i