#!/bin/bash
#sends a GET request then display the the body if sratus is 200
curl -s -X GET -L "$1"
