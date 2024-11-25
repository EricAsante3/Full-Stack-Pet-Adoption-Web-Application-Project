import React, { useEffect, useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'
import { useNavigate } from "react-router-dom";


interface CardProps {
  id: number;
  name: string;
  age: number;
  gender: string;
  species: string;
  location: string;
  photo: string;
  breed: string;
  paragraph: string;
  timestamp: string;
}

// Card Component
const Card: React.FC<CardProps> = ({
  id,
  name,
  age,
  gender,
  species,
  photo,
  breed,
  paragraph,
}) => {

  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/detailed/${id}`, {
      state: { id, name, age, gender, species, photo, breed },
    });
  };


  const handleunFavorite = async(pet_id: number) => {
    
    

    if (sessionStorage.getItem("userId") == null) {
      alert('Must be signed in, to access this feature');
      } else {
        console.log(`UserId: ${sessionStorage.getItem("userId")}, PetId: ${pet_id}`);


        const response = await fetch('http://localhost:5170/remove_favorite', {
        method: 'DELETE',
        headers: {
                'Content-Type': 'application/json', // Specify that you're sending JSON data
            },
          body: JSON.stringify({"user_id": sessionStorage.getItem("userId"),
                                "pet_id": pet_id}), // Convert payload to JSON string
          });

          window.location.reload();
      }



  };

  return (
    <div className="card2" onClick={handleCardClick}>
      <img className="card_image2" src={photo} alt="picture" style={{ width: "70%", height: "80%", objectFit: "cover" }} />
        <div style={{ maxHeight: "100%" }} className="card_attributes2">
            <h1 className="card_name">{name}</h1>
            <p className="card_info">Age: {age}</p>
            <p className="card_info">Gender: {gender}</p>
            <p className="card_info">Species: {species}</p>
            <p className="card_info">breed: {breed}</p>
            <Button style={{ maxHeight: "100%" }} className="r_button"           onClick={(e) => {
            e.stopPropagation(); // Prevent triggering `handleCardClick`
            handleunFavorite(id);
          }}
        >
            &#10005; Remove
            </Button>
        </div>

    </div>
  );
};

export default Card;
