#!/usr/bin/python3
""" this script is used to send a post request to a given
URL with the email as a parameter and display the response body
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    val = {}
    val["email"] = sys.argv[2]
    d = urllib.parse.urlencode(val)
    d = d.encode('ascii')
    req = urllib.request.Request(sys.argv[1], d)
    with urllib.request.urlopen(req) as response:
        data = response.read()
    print(data.decode("utf-8"))
