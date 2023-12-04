#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for a in matrix:
        i = 0
        while(i < len(a)):
            print("{:d}".format(a[i]), end="")
            i += 1
            if i != len(a):
                print(" ", end="")
        print()
