#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if (b > a):
            print("{}{}".format(a, b), end="")
            print(", " if ((b != 9) or (b - a != 1)) else "\n", end="")
