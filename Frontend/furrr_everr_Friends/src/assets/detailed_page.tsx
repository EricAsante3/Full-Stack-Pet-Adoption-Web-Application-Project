import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Header from './components/Header.tsx'; // Adjust the path if needed
import Filter from "./components/Filter.tsx"; // Adjust the path if needed
import { Link } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button'


// Define the structure for the pet's information
interface PetInfo {
  id: number;
  name: string;
  age: number;
  gender: string;
  species: string;
  location: string;
  photo: string;
  breed: string;
  description: string;
  timestamp: string;
}

const Detailed_Page: React.FC = () => {
  const { petId } = useParams<{ petId: string }>(); // Extract petId from URL
  const [petInfo, setPetInfo] = useState<PetInfo | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!petId) {
      setError("Pet ID not found in URL.");
      setLoading(false);
      return;
    }

    const fetchPetInfo = async () => {
      try {
        const response = await fetch("http://localhost:5170/fetch_pet", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ pet_id: petId }), // Sending petId as part of the POST body
        });

        if (!response.ok) {
          throw new Error("Failed to fetch pet information. Please try again later.");
        }

        const data = await response.json();

        // Transform the response into a structured object
        const transformedData: PetInfo = {
          id: data[0],
          name: data[1],
          age: data[2],
          gender: data[3],
          species: data[4],
          location: data[5],
          photo: data[6],
          breed: data[7],
          description: data[8],
          timestamp: data[9],
        };

        setPetInfo(transformedData);
        setLoading(false);
      } catch (err: any) {
        setError(err.message || "An error occurred while fetching pet information.");
        setLoading(false);
      }
    };

    fetchPetInfo();
  }, [petId]); // Dependency on petId

  if (loading) return <p>Loading pet details...</p>;
  if (error) return <p>Error: {error}</p>;

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




  const handleAdopt = async () => {
    alert(`Congratulations on your new pet, ${petInfo?.name}!`);
  };




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

        {petInfo && (
          <div className="card shadow-sm"     style={{
            display: "flex",
            flexDirection: "row",
            height: "80vh", // Specify the unit (e.g., px)
            maxHeight: "80vh", // This is fine as it includes a valid unit
            width: "100vw", // Specify the unit (e.g., px)
            maxWidth: "100vw", // Corrected camelCase
          }}>
            <img
              src={petInfo.photo}
              alt={`${petInfo.name}`}
              className="card-img-top img-fluid"
              style={{ width: "70%", height: "100%", objectFit: "cover" }}
            />
            <div className="card-body" >
              <h2>{petInfo.name}</h2>
              <p><strong>Breed:</strong> {petInfo.breed}</p>
              <p><strong>Location:</strong> {petInfo.location}</p>
              <p><strong>Age:</strong> {petInfo.age} years</p>
              <p><strong>Gender:</strong> {petInfo.gender}</p>
              <p>{petInfo.description}</p>
              <p><strong>Last Updated:</strong> {new Date(petInfo.timestamp).toLocaleString()}</p>
              
              <button className="btn r_button me-3"           onClick={(e) => {
                e.stopPropagation(); // Prevent triggering `handleCardClick`
                handleFavorite(petInfo.id);
              }}
              >&#9825; Favorite</button>
              <button className="btn btn-success" onClick={handleAdopt}>Adopt Me!</button>

              
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Detailed_Page;
