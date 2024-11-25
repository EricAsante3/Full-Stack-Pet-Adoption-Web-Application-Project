// src/Layout.tsx
// Imports
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CardContainer  from './components/AnimalView.tsx'; // Adjust the path if needed
import Filter from './components/Filter.tsx'; // Adjust the path if needed
import Header from './components/Header.tsx'; // Adjust the path if needed
import 'bootstrap/dist/css/bootstrap.min.css';


// TypeScript functional component
const HomePage: React.FC = () => {
  const [filter, setFilter] = useState<{ gender?: string; species?: string }>({});

  return (
    <div className="layout">

        <div className="content_header">
          <Header />
          <div className="separator_horizontal"></div>
        </div>

        <div className="content_pets">
          <Filter onFilterChange={(newFilter) => setFilter(newFilter)} />
          <div className="separator_vertical"></div>
          <CardContainer filter={filter} />
        </div>
    
    </div>

  );
};

export default HomePage;
