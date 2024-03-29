#!/usr/bin/python3
""" this script will fetch https://alx-intranet.hbtn.io/status from the web"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content_type = response.getheader('Content-Type').split(' ')[1]
    data = response.read()

print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data))
print("\t- utf8 content: {}".format(data.decode("utf-8")))
