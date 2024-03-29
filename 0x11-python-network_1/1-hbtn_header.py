#!/usr/bin/python3
""" this script will send a request to a given URL and
    displays the X-Request-Id header variable
"""


from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        request_id = response.getheader('X-Request-Id')

    print(request_id)
