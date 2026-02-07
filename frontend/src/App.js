import React from 'react';
import Navbar from './components/Navbar';
import MapView from './components/MapView';
import RiskAlert from './components/RiskAlert';
import Footer from './components/Footer';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <MapView />
      <RiskAlert alert="High Risk Area Ahead!" />
      <Footer />
    </div>
  );
}

export default App;
