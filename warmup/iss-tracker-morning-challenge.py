#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
from pprint import pprint
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    pprint(resp)
    print("\n\n")
    #pprint("lat " + {resp['iss_position']})
    timestamp = resp['timestamp']
    latitude = resp["iss_position"]["latitude"]
    longitude = resp["iss_position"]["longitude"]
  
    print(f"CURRENT LOCATION OF THE ISS:\n{timestamp}\nLon: {longitude}\nLat: {longitude}")

if __name__ == "__main__":
    main()