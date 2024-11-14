import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

function Dashboard() {
  const location = useLocation();
  const navigate = useNavigate();
  const userData = location.state?.userData;

  if (!userData) {
    return (
      <div>
        <h2>No user data found.</h2>
        <button onClick={() => navigate('/')}>Return to Login</button>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      <h2>Welcome, {userData.name}!</h2>
      <p><strong>Age:</strong> {userData.age}</p>
      <p><strong>Location:</strong> {userData.location}</p>
      <p><strong>Occupation:</strong> {userData.occupation}</p>
    </div>
  );
}

export default Dashboard;
