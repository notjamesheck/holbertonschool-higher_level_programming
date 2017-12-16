#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        comp = 0
        for x, y in my_dict.items():
            if y > comp:
                comp = y
                high = x
        return high
