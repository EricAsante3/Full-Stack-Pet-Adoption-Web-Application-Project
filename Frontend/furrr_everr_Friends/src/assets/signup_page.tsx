// src/Layout.tsx
// Imports
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Signup from "./components/Signup.tsx"; // Adjust the path if needed

// TypeScript functional component
const Signup_Page: React.FC = () => {
  return (
    <Signup />
  );
};

export default Signup_Page;
