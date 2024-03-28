#!/bin/bash
#get requst with header variable X-Sxhool-User-Id = 98
curl -X GET -s -H "X-School-User-Id: 98" "$1"
