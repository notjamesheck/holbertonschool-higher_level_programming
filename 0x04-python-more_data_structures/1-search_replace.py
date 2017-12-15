#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        copy = my_list[:]
        for i in range(len(copy)):
            if copy[i] == search:
                copy[i] = replace
        return copy
    return my_list
