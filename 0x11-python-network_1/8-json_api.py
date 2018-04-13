#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == '__main__':

    data = {'q': ""}
    if len(sys.argv) > 1:
        r = requests.post('http://172.31.54.208:38344/search_user',
                          data={'q': sys.argv[1]})
        '''
        try:
        '''
        sumVar = r.json()
        if sumVar:
            print('[{}] {}'.format(sumVar['id'], sumVar['name']))
        else:
            print('Not a valid JSON')
        '''
        except Exception:
            print('Not a valid JSON')
        '''
    else:
        print('No result')
