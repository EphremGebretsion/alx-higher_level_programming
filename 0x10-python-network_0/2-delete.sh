#!/bin/bash
#sends a delete request to the given URL
curl -X DELETE -L -s "$1"
