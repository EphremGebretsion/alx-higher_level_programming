#!/usr/bin/python3
indx = 97
while (indx < 123):
    if (indx == 101 or indx == 113):
        indx += 1
        continue
    print("{}".format(chr(indx)), end="")
    indx += 1
