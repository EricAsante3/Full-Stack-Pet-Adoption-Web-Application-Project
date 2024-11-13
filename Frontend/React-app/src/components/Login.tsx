import React, { useState } from 'react';
import '../App.css';  // Go up one directory level

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const response = await fetch('/fetch_userid', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (response.ok) {
      const userId = await response.json();
      window.location.href = `/user/${userId}`;
    } else {
      alert('Login failed!');
    }
  };

  return (
    <div className="container">
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <input type="text" name="username" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
          <input type="password" name="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <button type="submit">Log in</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
