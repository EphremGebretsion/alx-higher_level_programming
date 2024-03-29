#!/usr/bin/python3
""" this script will take a URL and send request and dispolay
the variable X-Request-Id in the response header"""


import requests
import sys

if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
