#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if '__name__' == '__main__':

    if sys.argv[1]:
        try:
            r = requests.post('http://34.206.234.184:38297/search_user',
                              data={'q': sys.argv[1]})
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
        except KeyError:
            print('Not a valid JSON')
    else:
        print('No result')
