#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dirList = dir(hidden_4)
    for i in dirList:
        if i.startswith("__"):
            continue
        print(i)
