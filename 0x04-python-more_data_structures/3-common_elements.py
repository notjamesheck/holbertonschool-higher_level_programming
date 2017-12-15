#!/usr/bin/python3
def common_elements(set_1, set_2):
    ret_str = []
    if not set_1:
        return
    if not set_2:
        return
    for i in set_1:
        for j in set_2:
            if i == j:
                ret_str.append(i)
    if not ret_str:
        return
    return ret_str
