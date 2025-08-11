import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import axios from 'axios';
import L from 'leaflet';

const healthyIcon = new L.Icon({
  iconUrl: 'https://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/green-dot.png',
  iconSize: [32, 32],
  iconAnchor: [16, 32],
  popupAnchor: [0, -32]
});

const ghostIcon = new L.Icon({
  iconUrl: 'https://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
  iconSize: [32, 32],
  iconAnchor: [16, 32],
  popupAnchor: [0, -32]
});

const BusMap = () => {
  const [buses, setBuses] = useState([]);
  const [hideGhosts, setHideGhosts] = useState(false);

  const fetchBuses = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/buses");
      setBuses(res.data.data);
    } catch (err) {
      console.error("Error fetching buses:", err);
    }
  };

  useEffect(() => {
    fetchBuses();
    const interval = setInterval(fetchBuses, 10000);
    return () => clearInterval(interval);
  }, []);

  const displayedBuses = hideGhosts ? buses.filter(b => !b.ghost) : buses;

  return (
    <div>
      <div style={{ padding: "10px", background: "#f5f5f5" }}>
        <label>
          <input
            type="checkbox"
            checked={hideGhosts}
            onChange={() => setHideGhosts(!hideGhosts)}
          />
          Hide Ghost Buses
        </label>
      </div>

      <MapContainer center={[-27.4705, 	153.0260]} zoom={12} style={{ height: "90vh", width: "100%" }}> {/*28.6139, 77.2090 - Delhi*/} {/*-27.4705, 	153.0260 - Brisbane*/} {/*1.4799, 103.7643 - Johor Bahru*/}
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {displayedBuses.map((bus) => (
          <Marker
            key={bus.id}
            position={[bus.lat, bus.lon]}
            icon={bus.ghost ? ghostIcon : healthyIcon}
          >
            <Popup>
              <b>Bus ID:</b> {bus.id} <br />
              <b>Lat:</b> {bus.lat} <br />
              <b>Lon:</b> {bus.lon} <br />
              <b>Last Update:</b> {new Date(bus.timestamp * 1000).toLocaleTimeString()} <br />
              <b>Status:</b> {bus.ghost ? "Ghost: " + bus.reason: "Active"}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default BusMap;
