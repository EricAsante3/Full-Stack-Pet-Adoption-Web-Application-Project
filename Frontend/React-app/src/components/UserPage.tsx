import React from 'react';
import { useParams } from 'react-router-dom';

const UserPage: React.FC = () => {
  const { userId } = useParams<{ userId: string }>();

  return (
    <div>Welcome, your user ID is {userId}</div>
  );
};

export default UserPage;
