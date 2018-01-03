#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for o in my_list:
        try:
            print("{:d}".format(o), end="")
            i += 1
            x -= 1
            if (x == 0):
                break
        except (ValueError, TypeError):
            x -= 0
            if (x == 0):
                break
            continue
    print()
    return i
