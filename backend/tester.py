from google.transit import gtfs_realtime_pb2

with open("test.pb", "rb") as f:
    data = f.read()

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(data)

print("Total entities:", len(feed.entity))

for entity in feed.entity[:5]:  # Show first 5 buses
    if entity.HasField('vehicle'):
        vehicle = entity.vehicle
        print({
            "id": vehicle.vehicle.id,
            "lat": vehicle.position.latitude,
            "lon": vehicle.position.longitude,
            "timestamp": vehicle.timestamp
        })