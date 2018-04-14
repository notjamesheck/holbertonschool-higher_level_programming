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
    # ah = r.json()['next']
    while (r):
        for d in r.json()['results']:
            print(d['name'])
        try:
            r = requests.get(r.json()['next'])
        except:
            break

    # [print(d) for d in r.json()['results']]
    # while r.json()['next']:
    #     r = requests.get(r.json()['next'])
    #     [print(d) for d in r.json()['results']]
