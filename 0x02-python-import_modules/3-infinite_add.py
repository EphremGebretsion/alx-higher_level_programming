#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    n = len(sys.argv)
    tot, i = 0, 1
    while (i < n):
        tot = tot + int(sys.argv[i])
        i += 1
    print("{}".format(tot))
