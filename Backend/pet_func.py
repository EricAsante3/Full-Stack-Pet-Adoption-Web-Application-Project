""" This module handles pet-related functionalities, providing details about random pets.
It uses the Flask framework to return pet information in a JSON format. """
from flask import jsonify

def get_random_pet():
    """Return a random pet's information."""
    randomint = "9"  # API generates a random integer representing a PET ID
    # API accesses database and returns information associated with the random ID
    # Returns information such as profile picture of the pet
    return jsonify({"id": randomint, "name": "Sam", "sex": "Male", "Age": "8",
                    "location": "Connecticut", "Breed": "Pug"})  # Return pet details
