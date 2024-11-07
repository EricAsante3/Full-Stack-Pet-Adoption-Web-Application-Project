"""
This module provides functions for HTTP communication and 
route functions
"""
import sqlite3
import databasefunctions
from flask import Flask, request, jsonify
from petfuc import get_random_pet
from userfuc import add_user_faviorte, remove_user_faviorte, replace_user_location
app = Flask(__name__)

# -----------------------------------------------------------------------------------------

@app.route("/add_newuser", methods=["POST"])
def add_newuser():
    """
    Adds new user to database
    """
    data = request.get_json()
    newuser_id = databasefunctions.insert_user(data.get("name"), data.get("age"), data.get("location"))

    return jsonify({'user_id': newuser_id}), 200  

@app.route("/add_newpet", methods=["POST"])
def add_newpet():
    """ 
    Adds new pet to database
    """
    data = request.get_json()
    newpet_id = databasefunctions.insert_pet(data.get("name"), data.get("age"),
                data.get("gender"), data.get("breed"), data.get("type"), 
                data.get("location"), data.get("photo_path"))

    return jsonify({'pet_id': newpet_id}), 200  


@app.route("/add_newfavorite", methods=["POST"])
def add_newfavorite():
    """ 
    Adds new user favorite to database
    """
    data = request.get_json()
    newfavorite_id = databasefunctions.insert_favorite(data.get("user_id"), data.get("pet_id"))

    return jsonify({'faviorte_id': newfavorite_id}), 200  



#------------------------------------------------------------------------------------------------

@app.route("/remove_user", methods=["DELETE"])
def removeuser():
    """
    Remove user from database
    """
    data = request.get_json()
    userid = data.get("user_id")
    roweffected = databasefunctions.remove_user(userid)

    return (f"{roweffected}, row was deleted in user table"), 200


@app.route("/remove_pet", methods=["DELETE"])
def removepet():
    """
    Remove pet from database
    """
    data = request.get_json()
    petid = data.get("petid")
    roweffected = databasefunctions.remove_pet(petid)

    return (f"{roweffected}, row was deleted in pet table"), 200


@app.route("/remove_favorite", methods=["DELETE"])
def removefavorite():
    """
    Remove favorite from database
    """
    data = request.get_json()
    roweffected = databasefunctions.remove_favorite(data.get("user_id"),data.get("pet_id"))

    return (f"{roweffected}, row was deleted in the favorite table"), 200

# ---------------------------------------------------------------------


@app.route("/fetch_pet", methods=["POST"])
def fetch_pet():
    """
    fetch pet from database
    """
    data = request.get_json()
    petid = data.get("pet_id")
    users_row = databasefunctions.fetch_pet_by_id(petid)

    return jsonify(users_row), 200  


@app.route("/fetch_user", methods=["POST"])
def fetch_user():
    """
    fetch user from database
    """
    data = request.get_json()
    userid = data.get("user_id")
    users_row = databasefunctions.fetch_user_by_id(userid)

    return jsonify(users_row), 200  


@app.route("/fetch_favorited_pets", methods=["POST"])
def fetch_favorite_pet():
    """
    fetches all pets favorited by a user 
    """
    data = request.get_json()
    userid = data.get("user_id")
    favorited_pets = databasefunctions.fetch_favorites_by_user(userid)

    return jsonify(favorited_pets), 200 


# ---------------------------------------------------------------


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
