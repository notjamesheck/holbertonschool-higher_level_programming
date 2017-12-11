#!/usr/bin/python3
import sys
count = 0
if len(sys.argv) > 1:
    for x in sys.argv:
        print("{}: {}".format(count, x))
        count += 1
