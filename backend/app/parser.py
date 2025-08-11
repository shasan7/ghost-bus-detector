import time
from google.transit import gtfs_realtime_pb2
from app.tracker import update_and_check_stationary

STALE_THRESHOLD = 300  # seconds

def parse_vehicle_positions(data):
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(data)

    buses = []
    now = time.time()

    for entity in feed.entity:
        if entity.HasField('vehicle'):
            vehicle = entity.vehicle
            ts = int(vehicle.timestamp)

            lat = float(vehicle.position.latitude)
            lon = float(vehicle.position.longitude)

            # Condition 1: stale GPS data
            stale = (now - ts) > STALE_THRESHOLD

            # Condition 2: stationary too long
            stationary = update_and_check_stationary(vehicle.vehicle.id, lat, lon)

            is_ghost = stale or stationary

            buses.append({
                "id": vehicle.vehicle.id,
                "lat": lat,
                "lon": lon,
                "timestamp": ts,
                "ghost": is_ghost,
                "reason": "Stale" if stale else ("Stationary" if stationary else "Active")
            })

    return buses
