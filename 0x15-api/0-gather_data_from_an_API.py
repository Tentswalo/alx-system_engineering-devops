#!/usr/bin/python3

'''A script that gathers data from an API.

'''

import re

import requests

import sys





API_URL = 'https://jsonplaceholder.typicode.com'

'''The API's URL.'''





if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        
        if re.fullmatch(r'\d+', sys.argv[1]):
            
            id = int(sys.argv[1])
            
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            
            todos_res = requests.get('{}/todos'.format(API_
