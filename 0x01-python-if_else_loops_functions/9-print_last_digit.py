#!/bin/bash/python3
def print_last_digit(number):
    base = 1
    number = abs(number)

    while (base < number):
        if (base * 10 > number):
            break
        base *= 10

    rem = number % base
    while (rem > 10):
        base //= 10
        rem %= base

    print(rem, end="")
    return rem
