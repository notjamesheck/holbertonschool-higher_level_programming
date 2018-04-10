#!/usr/bin/python3
'''
    comment
'''
import requests
import sys


r = requests.get(sys.argv[1])
if r.status_code is 200:
    print(r.text)
else:
    print(r.status_code)
