#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        newl = my_list[:]
        r = replace
        if search > 0:
            s = search - 1
        else:
            s = search
        for i in newl:
            if i == s:
                newl[i] = r
                break
        return newl
    else:
        return my_list
