#!/usr/bin/python3
'''
    comment
'''
import urllib
from urllib import request
from urllib import parse
import sys

email = { 'email' : sys.argv[2] }
email_data = parse.urlencode(email)
email_data = email_data.encode('ascii')
req = request.Request(sys.argv[1], email_data)
with request.urlopen(req) as data:
    fuuuu = data.read()
    print(fuuuu)
