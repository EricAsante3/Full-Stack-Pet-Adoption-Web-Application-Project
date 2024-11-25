import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../Signup.css';

function Signup() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [first_name, setfirst_name] = useState('');
  const [last_name, setlast_name] = useState('');
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();

    // Ensure passwords match
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    // Make API call to add_newuser
    try {
      const response = await fetch('http://localhost:5170/add_newuser', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username,
          password,
          first_name,
          last_name
        }),
      });

      if (response.ok) {
        const result = await response.json();
        console.log('User ID:', result.user_id); // Log user_id to confirm successful signup
        navigate('/'); // Redirect to login page
      } else {
        console.error('Signup failed');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="signup-container">
      <h2>Create an Account</h2>
      <form onSubmit={handleSignup}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="First Name"
          value={first_name}
          onChange={(e) => setfirst_name(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Last Name"
          value={last_name}
          onChange={(e) => setlast_name(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Confirm Password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
        <button type="submit">Create an Account</button>
      </form>
      <p>Already have an account? <a href="/" onClick={() => navigate('/')}>Log in</a></p>
    </div>
  );
}

export default Signup;
