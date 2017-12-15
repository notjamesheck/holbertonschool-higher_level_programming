#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = my_list[:]
    r = replace
    if search > 0:
        s = search - 1
    else:
        s = search
    for i in newl:
        if newl[i] == newl[s]:
            newl[s] = r
            break
    return newl
