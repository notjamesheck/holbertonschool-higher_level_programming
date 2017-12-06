#!/usr/bin/python3
for a in range(100):
    print('{:02d}'.format(a), end="")
    print(", " if (a != 99) else "\n", end="")
