#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == '__main__':

    r = requests.get('https://swapi.co/api/people/?search={}'.
                     format(sys.argv[1]))
    print('Number of results: {}'.format(r.json()['count']))
    results = r.json()['results']
    for val in results:
        print(val['name'])
