import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './home_page.tsx'
import Favorites_Page from './favorites_page.tsx';
import Detailed_Page from './detailed_page.tsx';
import Signup_Page from './signup_page.tsx';



const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/favorite" element={<Favorites_Page />} />
        <Route path="/detailed/:petId" element={<Detailed_Page />} />
        <Route path="/signup" element={<Signup_Page />} />
      </Routes>
    </Router>

  );
};

export default App;
