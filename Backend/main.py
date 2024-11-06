"""
This module provides functions for HTTP communication and route functions.
"""
from flask import Flask, request, jsonify
from flasgger import Swagger
from petfuc import get_random_pet
from userfuc import add_user_faviorte, remove_user_faviorte, replace_user_location

app = Flask(__name__)
Swagger(app)  # Initialize Swagger

# Get Random Pet information - For homepage
@app.route("/Get_Random_pet", methods=["GET"])
def random_pet():
    """
    Retrieve a random pet's information for the homepage.
    ---
    responses:
      200:
        description: Returns random pet information successfully.
        schema:
          type: object
          properties:
            name:
              type: string
              example: 'Rex'
            breed:
              type: string
              example: 'Dog'
            age:
              type: integer
              example: 5
    """
    return get_random_pet(), 200

# Favorites route. Add user favorite pet to database
@app.route("/Add_User_Faviorte", methods=["POST"])
def adduserfaviorte():
    """
    Add a pet to the user's favorites in the database.
    ---
    parameters:
      - in: body
        name: pet
        required: true
        schema:
          type: object
          properties:
            pet_id:
              type: integer
              example: 101
    responses:
      200:
        description: Pet added to favorites successfully.
    """
    json_data = request.get_json()
    return jsonify(add_user_faviorte(json_data)), 200

# Unfavorite Route. Remove user favorite pet from their database
@app.route("/Remove_User_Faviorte", methods=["DELETE"])
def removeuserfaviorte():
    """
    Remove a pet from the user's favorites in the database.
    ---
    parameters:
      - in: body
        name: pet
        required: true
        schema:
          type: object
          properties:
            pet_id:
              type: integer
              example: 101
    responses:
      200:
        description: Pet removed from favorites successfully.
    """
    json_data = request.get_json()
    return jsonify(remove_user_faviorte(json_data)), 200

# Change a User's account location
@app.route("/Change_User_Location", methods=["PUT"])
def replace_user_information():
    """
    Change the location associated with a user's account.
    ---
    parameters:
      - in: body
        name: location
        required: true
        schema:
          type: object
          properties:
            new_location:
              type: string
              example: 'New York, NY'
    responses:
      200:
        description: User location updated successfully.
    """
    newlocation = request.get_json()
    return jsonify(replace_user_location(newlocation)), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
