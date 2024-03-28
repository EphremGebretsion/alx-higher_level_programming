#!/bin/bash
#HTTPS post request with email and subeject variable for a given URL
curl -X POST -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
