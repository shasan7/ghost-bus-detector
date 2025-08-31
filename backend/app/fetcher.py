import os
import requests
from dotenv import load_dotenv

# GTFS-RT URLs of different cities
# https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb # Delhi's GTFS-RT, requires API Key, throttles down if too many requests
# https://gtfsrt.api.translink.com.au/api/realtime/SEQ/VehiclePositions/Bus # Translink's GTFT-RT in Southeast Queensland, Australia, includes Birsbane, Gold Coast and Sunshine Coast's buses' position
# https://api.data.gov.my/gtfs-realtime/vehicle-position/mybas-johor # GTFS-RT of Malaysia's Mybas-Johor's buses

# Delhi's API Keys - (Rest two don't need API Keys)
# Key: AbbCqRmImmkGK56JFVsUW8F1Fl6nZW5g
# Another Key: PGIQzUg2otOPdpkp35swgAcdIURGwaTd 

load_dotenv()

def fetch_gtfs_feed():
    url = "https://gtfsrt.api.translink.com.au/api/realtime/SEQ/VehiclePositions/Bus" # ?key=API_KEY , only for Delhi
    print(f"Fetching from: {url}")  # Debug
    response = requests.get(url)
    print(f"Status code: {response.status_code}, Bytes: {len(response.content)}")  # Debug
    response.raise_for_status()
    return response.content
