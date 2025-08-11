import os
import requests
from dotenv import load_dotenv

load_dotenv()

GTFS_URL = os.getenv("GTFS_URL")
API_KEY = os.getenv("GTFS_API_KEY")

def fetch_gtfs_feed():
    url = f"{GTFS_URL}?key={API_KEY}" #?key={API_KEY}
    print(f"Fetching from: {url}")  # Debug
    response = requests.get(url)
    print(f"Status code: {response.status_code}, Bytes: {len(response.content)}")  # Debug
    response.raise_for_status()
    return response.content
