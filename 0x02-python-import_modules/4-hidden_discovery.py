#!/usr/bin/python3
import hidden_4

if (__name__ == "__main__"):
    data = dir(hidden_4)

    for d in data:
        if (d[0] != "_" and d[1] != "__"):
            print("{}".format(d))
