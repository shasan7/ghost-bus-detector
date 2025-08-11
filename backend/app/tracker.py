import time
from math import radians, sin, cos, sqrt, atan2

# Store last position and last movement time for each bus
bus_history = {}

# Haversine formula to calculate distance in meters between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # meters
    phi1, phi2 = radians(lat1), radians(lat2)
    d_phi = radians(lat2 - lat1)
    d_lambda = radians(lon2 - lon1)

    a = sin(d_phi / 2)**2 + cos(phi1) * cos(phi2) * sin(d_lambda / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def update_and_check_stationary(bus_id, lat, lon):
    now = time.time()
    stationary_threshold_seconds = 300  # 5 minutes
    movement_threshold_meters = 30      # ~ bus length

    if bus_id not in bus_history:
        bus_history[bus_id] = {
            "lat": lat,
            "lon": lon,
            "last_move_time": now
        }
        return False  # not stationary yet

    prev = bus_history[bus_id]
    distance = haversine(lat, lon, prev["lat"], prev["lon"])

    if distance > movement_threshold_meters:
        # Bus moved — update position & reset timer
        bus_history[bus_id] = {
            "lat": lat,
            "lon": lon,
            "last_move_time": now
        }
        return False
    else:
        # Bus hasn't moved
        idle_time = now - prev["last_move_time"]
        if idle_time > stationary_threshold_seconds:
            return True  # stationary for too long
        else:
            return False
