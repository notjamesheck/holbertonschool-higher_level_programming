#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) > 1:
        for x in sys.argv[1:]:
            sum += int(x)
        print("{}".format(sum))

    elif len(sys.argv) <= 1:
        print("0")
