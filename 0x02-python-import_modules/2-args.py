#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("1 argument")
        elif len(sys.argv) > 1:
            print("{} arguments".format(len(sys.argv) - 1))
        for x in sys.argv[1:]:
            count += 1
            print("{}: {}".format(count, x))
    else:
        print("0 arguments")
