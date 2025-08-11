import time
from app.fetcher import fetch_gtfs_feed
from app.parser import parse_vehicle_positions

if __name__ == "__main__":
    while True:
        print("Fetching GTFS feed...")
        raw_data = fetch_gtfs_feed()
        if raw_data:
            buses = parse_vehicle_positions(raw_data)
            print(f"Got {len(buses)} buses")
            for bus in buses[:5]:
                print(bus)
        else:
            print("No data returned")
        time.sleep(10)