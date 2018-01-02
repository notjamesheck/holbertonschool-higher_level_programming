#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while True:
        try:
            if x and my_list[i]):
                if int(my_list[i]):
                     print("{:d}".format(my_list[i]), end="")
                i += 1
                x -= 1
        except:
            return i
