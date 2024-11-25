import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'

const Card: React.FC<CardProps> = ({
  id,
  name,
  age,
  gender,
  species,
  photo,
  breed,
}) => {
  const navigate = useNavigate();

  const handleFavorite = async (pet_id: number) => {
    if (sessionStorage.getItem("userId") == null) {
      alert("Must be signed in, to access this feature");
    } else {
      console.log(
        `UserId: ${sessionStorage.getItem("userId")}, PetId: ${pet_id}`
      );

      await fetch("http://localhost:5170/add_newfavorite", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: sessionStorage.getItem("userId"),
          pet_id: pet_id,
        }),
      });
    }
  };

  const handleCardClick = () => {
    navigate(`/detailed/${id}`, {
      state: { id, name, age, gender, species, photo, breed },
    });
  };

  return (
    <div className="card main" onClick={handleCardClick}>
      <img className="card_image" src={photo} alt={`${species}_picture`} style={{ width: "500px", height: "100px", objectFit: "cover" }}/>
      <h1 className="card_name">{name}</h1>
      <div className="card_attributes">
        <div>
          <p className="card_info">Age: {age}</p>
          <p className="card_info">Gender: {gender}</p>
          <p className="card_info">Species: {species}</p>
          <p className="card_info">Breed: {breed}</p>
          <Button className="r_button"
          onClick={(e) => {
            e.stopPropagation(); // Prevent triggering `handleCardClick`
            handleFavorite(id);
          }}
        >
          &#9825; Favorite
        </Button>
      </div>
        </div>

    </div>
  );
};

export default Card;
