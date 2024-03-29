#!/bin/bash
#json POST using curl
curl -s -X POST -F "@file=$2" "$1"
