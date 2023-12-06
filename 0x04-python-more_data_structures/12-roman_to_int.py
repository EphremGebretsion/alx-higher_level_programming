#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    decimal_places = {"MMM": 3000, "MM": 2000, "M": 1000,
                      "CM": 900, "DCCC": 800, "DCC": 700, "DC": 600, "D": 500,
                      "CD": 400, "CCC": 300, "CC": 200, "C": 100,
                      "XC": 90, "LXXX": 80, "LXX": 70, "LX": 60, "L": 50,
                      "XL": 40, "XXX": 30, "XX": 20, "X": 10, "IX": 9,
                      "VIII": 8, "VII": 7, "VI": 6, "V": 5, "IV": 4,
                      "III": 3, "II": 2, "I": 1}
    roman = roman_string[:]
    num = 0
    for key in decimal_places:
        if (not len(roman)):
            break
        if (len(roman) >= len(key)):
            if (roman[:len(key)] == key):
                num += decimal_places[key]
                roman = roman[len(key):]
    return num
