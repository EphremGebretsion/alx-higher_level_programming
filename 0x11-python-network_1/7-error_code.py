#!/usr/bin/python3
""" this script takes in a URL, sends a request to the URL and
displays the body of the response if HTTP status code is
not greater than or equal to 400"""


import requests
import sys

if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    if (r.status_code < 400):
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
