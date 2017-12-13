#!/usr/bin/python
def uppercase(str):
    s = list(str)
    for l in range(len(s)):
        if ((ord(s[l]) >= 97) and (ord(s[l]) <= 122)):
                s[l] = ord(s[l]) - 32
                s[l] = chr(s[l])
    blah = "".join(s)
    print("{}".format(blah))    
