#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if sys.argv[1]:
    r = requests.post('http://34.206.234.184:38297/search_user', data={'q': sys.argv[1]})
    print('[{}] {}'.format(r.json()['id'], r.json()['name']))

if r.json() is None and sys.argv[1]:
    r = requests.post('http://34.206.234.184:38297/search_user', data={'q': sys.argv[1]})
    print('Not a valid JSON')
elif r.json() is None:
    print('No result')
