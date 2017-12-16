#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        sump = 0
        itera = list(roman_string)
        for a in itera:
            if a == 'I':
                sump += 1
            elif a == 'V':
                sump += 5
            elif a == 'X':
                sump += 10
            elif a == 'L':
                sump += 50
            elif a == 'C':
                sump += 100
            elif a == 'D':
                sump += 500
            elif a == 'M':
                sump += 1000
    return sump
