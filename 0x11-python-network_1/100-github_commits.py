#!/usr/bin/python3
"""
lists 10 commits from recent to oldest of a given repository
and user name using GitHub API
"""


import requests
import sys

if __name__ == "__main__":
    REPO = sys.argv[1]
    OWNER = sys.argv[2]
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    resp = requests.get(url)
    res = resp.json()
    last = 10
    if len(res) < last:
        last = len(res)
    i = 0
    while i < last:
        sha = res[i]["sha"]
        author_name = res[i]["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
        i += 1
