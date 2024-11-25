import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './assets/app.tsx';  // Corrected path if your App.tsx is in the assets folder
import './assets/styles.css';  // Assuming you have a styles.css

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
