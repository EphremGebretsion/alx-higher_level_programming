#!/usr/bin/python3
def uppercase(str):
    strLen, i, asii = len(str), 0, 0
    newchr = str
    while (i < strLen):
        newchr = str[i]
        asii = ord(str[i])
        if (asii > 96 and asii < 123):
            newchr = chr(ord(str[i]) - 32)
        print("{}".format(newchr), end="")
        i += 1
    print("{}".format(""))
