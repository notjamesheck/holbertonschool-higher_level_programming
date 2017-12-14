#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        leng = len(i) - 1
        for j in i:
            if leng != 0:
                print("{:d}".format(j), end=" ")
                leng -= 1
            else:
                print("{:d}".format(j), end="")
        print()
