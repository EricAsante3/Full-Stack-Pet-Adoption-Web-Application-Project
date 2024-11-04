"""
This module provides functions for HTTP communication and 
route functions
"""
from flask import jsonify


def get_random_pet():
    """
    Function to generate random ID and return pet
    asscoieted with that ID
    """
    randomint = "9" # APi generates random interger that represents a PET ID
    # Api accesses database and return information in data base
    #Retrun information such as profile picture on the pet accosiated with the random ID
    data = {"id": randomint,
            "name":"sam",
            "sex":"male",
            "Age":"8", 
            "location":"Connecticwut", 
            "Breed": "Pug"}
    return jsonify(data) # Return dog information
