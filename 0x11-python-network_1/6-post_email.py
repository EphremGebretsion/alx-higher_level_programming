#!/usr/bin/python3
""" this script will take a URL and an email address and sends
a post request to the passed URL with the email as a paraeter
and display the body of response"""


import requests
import sys

if __name__ == "__main__":
    values = {}
    values["email"] = sys.argv[2]

    r = requests.post(sys.argv[1], data=values)
    print(r.text)
