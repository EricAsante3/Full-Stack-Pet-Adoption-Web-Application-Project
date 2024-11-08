"""
This module provides functions for HTTP communication and 
route functions
"""
from flask import Flask, request, jsonify
from database_files import databasefunctions
app = Flask(__name__)

# -----------------------------------------------------------------------------------------

@app.route("/add_newuser", methods=["POST"])
def add_newuser():
    """
    Adds new user to database
    """
    data = request.get_json()
    newuser_id = databasefunctions.insert_user(data.get("username"),data.get("password"),
                                               data.get("name"), data.get("age"),
                                               data.get("location"))

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
    INSERT INTO pets (name, age, gender, breed, type, location, photo_path)
    VALUES 
    ('Bella', 3, 'female', 'Golden Retriever', 'dog', 'New York', 'images/Chuck.jpg'),
    ('Max', 5, 'male', 'Maine Coon', 'cat', 'Boston', 'images/gunner.jpg'),
    ('Luna', 2, 'female', 'Siamese', 'cat', 'Chicago', 'images/luna.jpg'),
    ('Charlie', 4, 'male', 'Beagle', 'dog', 'Los Angeles', 'images/lizzie_izzie.jpg'),
    ('Daisy', 1, 'female', 'Labrador Retriever', 'dog', 'Miami', 'images/monster.jpg');

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
    petid = data.get("pet_id")
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



@app.route("/fetch_userid", methods=["POST"])
def fetch_userid():
    """
    fetch userid associated with username and password 
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")


    userid = databasefunctions.fetch_userid_from_username_and_password(username, password)

    return jsonify(userid), 200





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

@app.route("/fetch_allusers", methods=["POST"])
def fetch_allusers():
    """
    fetches all users in database 
    """

    allusers = databasefunctions.fetch_all_users()
    return jsonify(allusers), 200


@app.route("/fetch_allpets", methods=["POST"])
def fetch_allpets():
    """
    fetches all pets in database 
    """

    allpets = databasefunctions.fetch_all_pets()
    return jsonify(allpets), 200







if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
