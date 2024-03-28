#!/bin/bash
#returns HTTP methods the server will accept
curl -X OPTIONS -s -i "$1" | grep Allow |cut -d ":" -f 2| cut -d " " -f 2-
