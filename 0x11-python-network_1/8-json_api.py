#!/usr/bin/python3
"""this script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
and display the id and name like this: [<id>] <name>"""


import requests
import sys

if(__name__ == "__main__"):

    if(len(sys.argv) < 2):
        print("No result")
    else:
        val = {}
        val["q"] = sys.argv[1]

        r = requests.post("http://0.0.0.0:5000/search_user", data=val)

        try:
            r.json()
        except ValueError as e:
            print("Not a valid JSON")
        else:
            to_dict = r.json()
            if (to_dict == {} or "id" not in to_dict or "name" not in to_dict):
                print("No result")
            else:
                print("[{}] {}".format(to_dict["id"], to_dict["name"]))
