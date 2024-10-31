from flask import Flask, json, request, jsonify
from PetFuc import Get_Random_Pet
from UserFuc import Add_User_Faviorte, Remove_User_Faviorte, Replace_User_Location

app = Flask(__name__)

#Get Random Pet information - For homepage
@app.route("/Get_Random_pet", methods=["GET"])
def get_random_pet():
    return Get_Random_Pet(), 200 # Return dog information

# Faviortes route. add user faviorte pet to database
@app.route("/Add_User_Faviorte", methods=["POST"])
def add_user_faviorte():
    json_data = request.get_json() 

    # Api accesses database and append post json in database
    #Retrun database with succses code
    return jsonify(Add_User_Faviorte(json_data)), 200

# Un Faviote Route. remove user faviorte pet from there database 
@app.route("/Remove_User_Faviorte", methods=["DELETE"])
def remove_user_faviorte():
    json_data = request.get_json() 

    # Api accesses database and append post json in database
    #Retrun database with succses code
    return jsonify(Remove_User_Faviorte(json_data)), 200 # return new user database 

# Change a Users account location
@app.route("/Change_User_Location", methods=["PUT"])
def replace_user_information():
    NewLocation = request.get_json() # Get new location from post request 
    return jsonify(Replace_User_Location(NewLocation)) # retrun user account info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
