import React, { useState } from 'react';
import '../App.css'; // Ensure this path is correct based on your project structure

interface SignupData {
  username: string;
  password: string;
  name: string;
  age: number;
  location: string;
}

const Signup: React.FC = () => {
  const [signupData, setSignupData] = useState<SignupData>({ username: '', password: '', name: '', age: 0, location: '' });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSignupData({ ...signupData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const response = await fetch('/add_newuser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(signupData),
    });

    if (response.ok) {
      window.location.href = '/login';
    } else {
      alert('Signup failed!');
    }
  };

  return (
    <div className="container">
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <input type="text" name="username" placeholder="Username" value={signupData.username} onChange={handleInputChange} required />
          <input type="password" name="password" placeholder="Password" value={signupData.password} onChange={handleInputChange} required />
          <input type="text" name="name" placeholder="Name" value={signupData.name} onChange={handleInputChange} required />
          <input type="number" name="age" placeholder="Age" value={signupData.age.toString()} onChange={handleInputChange} required />
          <input type="text" name="location" placeholder="Location" value={signupData.location} onChange={handleInputChange} required />
          <button type="submit">Create an account</button>
        </form>
      </div>
    </div>
  );
};

export default Signup;
