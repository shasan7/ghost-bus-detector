from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from app.fetcher import fetch_gtfs_feed
from app.parser import parse_vehicle_positions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cached_buses = []
last_update_time = 0
CACHE_INTERVAL = 10  # seconds

@app.get("/buses")
def get_buses():
    global cached_buses, last_update_time
    now = time.time()
    if now - last_update_time > CACHE_INTERVAL:
        raw_data = fetch_gtfs_feed()
        if raw_data:
            cached_buses = parse_vehicle_positions(raw_data)
            last_update_time = now
    return {"count": len(cached_buses), "data": cached_buses}
