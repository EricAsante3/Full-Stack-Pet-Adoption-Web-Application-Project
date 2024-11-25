// src/Layout.tsx
// Imports
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Filter from './components/Filter.tsx'; // Adjust the path if needed
import CardContainer  from './components/FaviorteView.tsx'; // Adjust the path if needed
import Header from './components/Header.tsx'; // Adjust the path if needed
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'

// TypeScript functional component
const Favorites_Page: React.FC = () => {
    const [filter, setFilter] = useState<{ gender?: string; species?: string }>({});

  return (
    <div className="layout">

        <div className="content_header">
            <Header />
            <div className="separator_horizontal"></div>
        </div>

        <div className="content_pets">
        <Link to="/">

          <Button
            className="g_button"
            style={{
              width: "9vw",
              maxWidth: "10vw",
              height: "10vh",
              maxHeight: "20vh",
              margin: "10px" 
            }}
          >
            &#8592; Animal View
          </Button>
        </Link>
          <div className="separator_vertical"></div>
          <CardContainer filter={filter} />
        </div>


    </div>

  );
};

export default Favorites_Page;
