#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb = number
if numb < 0:
    ones = abs(numb) % 10
    ones = ones * -1
else:
    ones = numb % 10

if ones > 5:
    print("Last digit of {} is {} and greater than 5".format(ones, numb))
elif ones < 6 and ones != 0:
    print("Last digit of {} is {} is less than 6 and not 0".format(ones, numb))
elif ones == 0:
    print("Last digit of {} is {} and is 0".format(ones, numb))
