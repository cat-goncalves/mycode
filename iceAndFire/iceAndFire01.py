#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
from pprint import pprint

AOIF = "https://www.anapioficeandfire.com/api/characters?name="

def main():
    character = input("Enter GoT Character Name: ")
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF + character)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    pprint(got_dj)

if __name__ == "__main__":
    main()
