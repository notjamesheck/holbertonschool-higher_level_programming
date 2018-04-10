#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print(r.text)
