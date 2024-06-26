#!/usr/bin/python3
"""
this script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == "__main__":
    a = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=a)
    d = r.json()
    print(d.get("id"))
