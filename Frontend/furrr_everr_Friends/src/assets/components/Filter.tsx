import React from "react";
import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css';

interface FilterProps {
  onFilterChange: (filter: { gender?: string; species?: string }) => void; // Callback to parent
}

const Filter: React.FC<FilterProps> = ({ onFilterChange }) => {
  return (
    <div className="Filter">
      <h3>Filters</h3>
      <Button className="y_button" onClick={() => onFilterChange({ species: "Dog" })}>Show Dogs</Button>
      <Button className="y_button" onClick={() => onFilterChange({ species: "Cat" })}>Show Cats</Button>
      <Button className="y_button" onClick={() => onFilterChange({ gender: "Male" })}>Show Males</Button>
      <Button className="y_button" onClick={() => onFilterChange({ gender: "Female" })}>Show Females</Button>
      <Button className="y_button" onClick={() => onFilterChange({})}>Show All</Button>
    </div>
  );
};

export default Filter;
