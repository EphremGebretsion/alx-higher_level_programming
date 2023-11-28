#!/usr/bin/python3

lower_case = 122
upper_case = 90
lower = True

while (upper_case >= 65):
    pr = upper_case
    if (lower):
        pr = lower_case

    print("{}".format(chr(pr)), end="")
    lower = not lower
    upper_case -= 1
    lower_case -= 1
