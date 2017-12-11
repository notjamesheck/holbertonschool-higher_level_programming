#!/usr/bin/python3
import sys
sum = 0
if len(sys.argv) > 1:
    for x in sys.argv:
        mint = eval(x)
        sum += mint
