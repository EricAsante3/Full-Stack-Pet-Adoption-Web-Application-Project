import React, { useEffect, useState } from "react";
import Card from "./card";
import Filter from "./Filter"; // Import the filter component

interface CardProps {
  id: number;
  name: string;
  age: number;
  gender: string;
  species: string;
  photo: string;
  breed: string;
}

interface CardContainerProps {
  filter: { gender?: string; species?: string }; // Accept filter as a prop
}

const CardContainer: React.FC<CardContainerProps> = ({ filter }) => {
  const [cardData, setCardData] = useState<CardProps[]>([]);
  const [filteredData, setFilteredData] = useState<CardProps[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:5170/fetch_allpets", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) throw new Error("Failed to fetch data");

        const data: any[][] = await response.json();
        const formattedData: CardProps[] = data.map((item) => ({
          id: item[0],
          name: item[1],
          age: item[2],
          gender: item[3],
          species: item[4],
          photo: item[6],
          breed: item[7],
        }));

        setCardData(formattedData);
        setFilteredData(formattedData);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    let filtered = [...cardData];
    if (filter.gender) filtered = filtered.filter((card) => card.gender === filter.gender);
    if (filter.species) filtered = filtered.filter((card) => card.species === filter.species);
    setFilteredData(filtered);
  }, [filter, cardData]);

  return (
    <div id="card-container">
      {filteredData.map((data) => (
        <Card
          key={data.id}
          id={data.id}
          name={data.name}
          age={data.age}
          gender={data.gender}
          species={data.species}
          photo={data.photo}
          breed={data.breed}
        />
      ))}
    </div>
  );
};

export default CardContainer;
