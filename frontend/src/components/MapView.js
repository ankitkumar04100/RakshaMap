import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import '../styles/MapView.css';

function MapView() {
  const position = [28.6139, 77.209]; // Delhi coords for example

  return (
    <div className="map-container">
      <MapContainer center={position} zoom={13} style={{ height: '500px', width: '100%' }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <Marker position={position}>
          <Popup>Sample High-Risk Area</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}

export default MapView;
