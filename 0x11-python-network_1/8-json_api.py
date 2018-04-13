#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        try:
            r = requests.post('http://172.31.54.208:38344/search_user',
                              data={'q': sys.argv[1]})
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
        except Exception:
            print('Not a valid JSON')
    else:
        print('No result')
