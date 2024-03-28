#!/bin/bash
# this bash script will display the size of body response
curl -I -s "$1" | grep Content-Length| cut -d " " -f 2
