// main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';  // Ensure this import path matches where your App.tsx file is located
import './index.css';    // Ensure you have an index.css or remove this line if not needed

const rootElement = document.getElementById('root');
if (!rootElement) throw new Error('Failed to find the root element');
const root = ReactDOM.createRoot(rootElement);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
