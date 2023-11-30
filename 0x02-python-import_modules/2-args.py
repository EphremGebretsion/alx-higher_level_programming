#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    n = len(sys.argv)
    i = 1
    if (n == 1):
        print("{} arguments.".format(n - 1))
    elif (n == 2):
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))
    if (n > 1):
        while (i < n):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
