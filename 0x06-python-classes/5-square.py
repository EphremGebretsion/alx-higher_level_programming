#!/usr/bin/python3
""" square class """

BaseSq = __import__("4-square").Square


class Square(BaseSq):
    def my_print(self):
        i = 0
        if (self.__size == 0):
            print("")
        else:
            while(i < self.__size):
                j = 0
                while(j < self.__size):
                    print("#", end="")
                    j += 1
                print("")
                i += 1
