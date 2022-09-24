#!/usr/bin/python3

"""
This is a Python script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""


import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1], data={'email': sys.argv[1]})
    if r.raise_for_status() == None:
        print(r.content.decode('utf-8'))
    else:
        print("Error Code".format(r.status_code))