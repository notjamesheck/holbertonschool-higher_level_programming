#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nu = number
if nu < 0:
    nt = abs(nu) % 10
    nt = nt * -1
else:
    nt = nu % 10

if nt > 5:
    print("Last digit of {} is {} and is greater than 5".format(nt, nu))
elif nt < 6 and nt != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(nt, nu))
elif nt == 0:
    print("Last digit of {} is {} and is 0".format(nt, nu))
