#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = my_list[:]
    for i in newl:
        if newl[i] == newl[search-1]:
            newl[search-1] = replace
            break
    return newl
