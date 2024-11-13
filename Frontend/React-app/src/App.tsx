// App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';     // Adjust these imports based on your folder structure
import Signup from './components/Signup';
import UserPage from './components/UserPage';
import './App.css';


const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/user/:userId" element={<UserPage />} />
        <Route path="/" element={<Signup />} />
      </Routes>
    </Router>
  );
};

export default App;
