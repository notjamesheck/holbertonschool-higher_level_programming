#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
listed = str.split(' ')
str = ("{} {} {} {}".format(listed[5], listed[6], listed[-4], listed[0]))
print(str)
