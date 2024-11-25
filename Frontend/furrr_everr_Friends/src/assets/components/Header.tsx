// src/BlueScreen.tsx
import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'
import { useNavigate } from "react-router-dom";

// TypeScript functional component
const Header: React.FC = () => {
    const navigate = useNavigate();

    // State for storing username and password
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(
      () => sessionStorage.getItem('isLoggedIn') === 'true' // Initialize from session storage
    );
    const [data2, setData2] = useState<any>(
      () => JSON.parse(sessionStorage.getItem('data2') || 'null')
    );





    useEffect(() => {
      // Sync isLoggedIn state with session storage whenever it changes
      sessionStorage.setItem('isLoggedIn', String(isLoggedIn));
    }, [isLoggedIn]);


    useEffect(() => {
      // Sync data2 state with session storage whenever it changes
      if (data2) {
        sessionStorage.setItem('data2', JSON.stringify(data2));
      } else {
        sessionStorage.removeItem('data2');
      }
    }, [data2]);

    // Handle form submission
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault(); // Prevent default form submission
      if (!username || !password) {
        alert('Both fields are required.');
        return;
     }
      const payload = {
        "username": username,
        "password": password,
     };


     const response = await fetch('http://localhost:5170/fetch_userid', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json', // Specify that you're sending JSON data
      },
      body: JSON.stringify(payload), // Convert payload to JSON string
      });
  

      const data = await response.json(); // Parse JSON response
      console.log('Response from server:', data); // Log response to console

      
      if (data == null) {
        alert('Credentials not associated with an account');
    } else {
      sessionStorage.setItem("userId", data);
      const response = await fetch('http://localhost:5170/fetch_user', {
      method: 'POST',
      headers: {
            'Content-Type': 'application/json', // Specify that you're sending JSON data
        },
      body: JSON.stringify({"user_id": data}), // Convert payload to JSON string
      });

      const data2 = await response.json(); // Parse JSON response
      setData2(data2);  // Store the fetched user data in state
      setIsLoggedIn(true);

    }
    };

    const handleLogout = () => {
      setIsLoggedIn(false); // Set isLoggedIn to false to logout
      setData2(null); // Clear user data
      sessionStorage.removeItem('isLoggedIn');
      sessionStorage.removeItem('userId');
      sessionStorage.removeItem('data2');
      navigate(`/`)

    };

  return (
    <div className="header">
      <img className="title_logo" src="/assets/images/title.png" alt="Title"></img>
      {!isLoggedIn ? (
      <div className="elements_header">
        <form onSubmit={handleSubmit} className="signsection">
          <div>
            <input
              className="form-control"
              placeholder="Username"
              type="text"
              id="username"
              value={username}
              
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div>
            <input
              className="form-control"
              placeholder="Password"
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="signin_button">
            <Button type="submit" className="y_button signin_button" >
              Sign In
            </Button>
          </div>

        </form>

        <div className="extra_header">


          <Link to="/signup" type="button" className="btn btn-link">Sign Up?</Link>
        </div>

      </div>
    ) : (
      <div className="elements_header">
        <div className='account_name'>
          {data2 && <h1>Welcome, {data2[3]} {data2[4]}!</h1>}
        </div>

        <div className="extra_header">
          <Link to="/favorite" type="button" className="btn btn-link">Faviortes Page</Link>
          <button onClick={handleLogout} type="button" className="btn btn-link">Sign Out</button>
        </div>
      </div>
    )}
    </div>
  );
};

export default Header;
