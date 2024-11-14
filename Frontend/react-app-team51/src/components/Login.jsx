import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Login.css';

function Login() {
  const [userId, setUserId] = useState('');
  const [userData, setUserData] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
        const response = await fetch('http://localhost:5000/fetch_user', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: parseInt(userId) }), // Ensure userID is correctly parsed
        });

        const data = await response.json();
        console.log(data);  // Log the full response data

        if (!response.ok) {
            throw new Error('Failed to fetch user details');
        }

        setUserData(data.user_details); // Assuming user_details is expected
        navigate('/dashboard', { state: { userData: data.user_details } });
    } catch (error) {
        console.error('Error:', error);
    }
};

  return (
    <div className="login-container">
      <h2>Log in</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />
        <button type="submit">Log In</button>
      </form>
      <p>Don't have an account? <a href="/signup" onClick={() => navigate('/signup')}>Sign up</a></p>
    </div>
  );
}

export default Login;
