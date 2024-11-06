"""
This module provides backend functions to manage pet-related data.
"""
from flask import jsonify

def get_random_pet():
    """
    Generates a random ID and returns information associated with that ID.
    This function simulates accessing a database to fetch pet information
    based on a randomly generated pet ID.
    
    Returns:
        dict: A dictionary containing pet data, suitable for JSON response.
        
    Example return:
        {
            "id": "9",
            "name": "Sam",
            "sex": "Male",
            "Age": "8",
            "location": "Connecticut",
            "Breed": "Pug"
        }
    """
    random_int = "9"  # API generates random integer that represents a PET ID
    data = {
        "id": random_int,
        "name": "Sam",
        "sex": "Male",
        "Age": "8",
        "location": "Connecticut",
        "Breed": "Pug"
    }
    return data  # Return pet information as a dictionary

