#!/usr/bin/python3
""" this script will fech https://alx-intranet.hbtn.io/status
using a requests module"""


import requests

if __name__ == "__main__":

    r = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
