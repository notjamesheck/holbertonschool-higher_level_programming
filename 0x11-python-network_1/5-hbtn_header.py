#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
