"""
This module provides functions for HTTP communication and 
route functions
"""
from flask import Flask, request, jsonify
from petfuc import get_random_pet
from userfuc import add_user_faviorte, remove_user_faviorte, replace_user_location

app = Flask(__name__)

#Get Random Pet information - For homepage
@app.route("/Get_Random_pet", methods=["GET"])
def random_pet():
    """
    Function to extract random pet information
    """
    return get_random_pet(), 200 # Return dog information

# Faviortes route. add user faviorte pet to database
@app.route("/Add_User_Faviorte", methods=["POST"])
def adduserfaviorte():
    """
    Function to add user from database
    """
    json_data = request.get_json()

    # Api accesses database and append post json in database
    #Retrun database with succses code
    return jsonify(add_user_faviorte(json_data)), 200

# Un Faviote Route. remove user faviorte pet from there database
@app.route("/Remove_User_Faviorte", methods=["DELETE"])
def removeuserfaviorte():
    """
    Function to remove user from database
    """
    json_data = request.get_json()

    # Api accesses database and append post json in database
    #Retrun database with succses code
    return jsonify(remove_user_faviorte(json_data)), 200 # return new user database

# Change a Users account location
@app.route("/Change_User_Location", methods=["PUT"])
def replace_user_information():
    """
    Function to change the location associated with
    an account
    """
    newlocation = request.get_json() # Get new location from post request
    return jsonify(replace_user_location(newlocation)) # retrun user account info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)