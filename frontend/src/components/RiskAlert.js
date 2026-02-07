import React from 'react';
import '../styles/RiskAlert.css';

function RiskAlert({ alert }) {
  return alert ? <div className="risk-alert">{alert}</div> : null;
}

export default RiskAlert;
