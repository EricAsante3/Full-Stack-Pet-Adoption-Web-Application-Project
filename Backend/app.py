"""
This module provides functions for HTTP communication and 
route functions.
"""
from flask import Flask, request, jsonify
from flasgger import Swagger
from database_files import databasefunctions

app = Flask(__name__)
Swagger(app)  # Initialize Swagger

# -----------------------------------------------------------------------------------------

@app.route("/add_newuser", methods=["POST"])
def add_newuser():
    """
    Adds a new user to the database.
    ---
    parameters:
      - name: username
        in: body
        type: string
        required: true
      - name: password
        in: body
        type: string
        required: true
      - name: name
        in: body
        type: string
        required: true
      - name: age
        in: body
        type: integer
        required: true
      - name: location
        in: body
        type: string
        required: true
    responses:
      200:
        description: User added successfully with generated user ID.
        schema:
          type: object
          properties:
            user_id:
              type: integer
              example: 1
    """
    data = request.get_json()
    newuser_id = databasefunctions.insert_user(data.get("username"), data.get("password"),
                                               data.get("name"), data.get("age"),
                                               data.get("location"))

    return jsonify({'user_id': newuser_id}), 200

@app.route("/add_newpet", methods=["POST"])
def add_newpet():
    """ 
    Adds a new pet to the database.
    ---
    parameters:
      - name: name
        in: body
        type: string
        required: true
      - name: age
        in: body
        type: integer
        required: true
      - name: gender
        in: body
        type: string
        required: true
      - name: breed
        in: body
        type: string
        required: true
      - name: type
        in: body
        type: string
        required: true
      - name: location
        in: body
        type: string
        required: true
      - name: photo_path
        in: body
        type: string
        required: false
    responses:
      200:
        description: Pet added successfully with generated pet ID.
        schema:
          type: object
          properties:
            pet_id:
              type: integer
              example: 101
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
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
      - name: pet_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: Favorite added successfully with generated favorite ID.
        schema:
          type: object
          properties:
            favorite_id:
              type: integer
              example: 201

    """
    data = request.get_json()
    newfavorite_id = databasefunctions.insert_favorite(data.get("user_id"), data.get("pet_id"))

    return jsonify({'favorite_id': newfavorite_id}), 200



#------------------------------------------------------------------------------------------------

@app.route("/remove_user", methods=["DELETE"])
def removeuser():
    """
    Remove user from database
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: User removed successfully.
        schema:
          type: object
          properties:
            row_effected:
              type: integer
              description: Number of rows deleted in user table.
              example: 1
    """
    data = request.get_json()
    userid = data.get("user_id")
    roweffected = databasefunctions.remove_user(userid)

    return (f"{roweffected}, row was deleted in user table"), 200


@app.route("/remove_pet", methods=["DELETE"])
def removepet():
    """
    Remove pet from database
    ---
    parameters:
      - name: pet_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: Pet removed successfully.
        schema:
          type: object
          properties:
            row_effected:
              type: integer
              description: Number of rows deleted in pet table.
              example: 1
    """
    data = request.get_json()
    petid = data.get("pet_id")
    roweffected = databasefunctions.remove_pet(petid)

    return (f"{roweffected}, row was deleted in pet table"), 200


@app.route("/remove_favorite", methods=["DELETE"])
def removefavorite():
    """
    Remove favorite from database
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
      - name: pet_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: Favorite removed successfully.
        schema:
          type: object
          properties:
            row_effected:
              type: integer
              description: Number of rows deleted in the favorite table.
              example: 1
    """
    data = request.get_json()
    roweffected = databasefunctions.remove_favorite(data.get("user_id"),data.get("pet_id"))

    return (f"{roweffected}, row was deleted in the favorite table"), 200

# ---------------------------------------------------------------------



@app.route("/fetch_userid", methods=["POST"])
def fetch_userid():
    """
    fetch userid associated with username and password 
    ---
    parameters:
      - name: username
        in: body
        type: string
        required: true
      - name: password
        in: body
        type: string
        required: true
    responses:
      200:
        description: User ID retrieved successfully.
        schema:
          type: object
          properties:
            user_id:
              type: integer
              example: 1
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
    ---
    parameters:
      - name: pet_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: Pet details retrieved successfully.
        schema:
          type: object
          properties:
            pet_details:
              type: object
              properties:
                name:
                  type: string
                age:
                  type: integer
                gender:
                  type: string
                breed:
                  type: string
                type:
                  type: string
                location:
                  type: string
                photo_path:
                  type: string
    """
    data = request.get_json()
    petid = data.get("pet_id")
    users_row = databasefunctions.fetch_pet_by_id(petid)

    return jsonify(users_row), 200


@app.route("/fetch_user", methods=["POST"])
def fetch_user():
    """
    fetch user from database
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: User details retrieved successfully.
        schema:
          type: object
          properties:
            user_details:
              type: object
              properties:
                name:
                  type: string
                age:
                  type: integer
                location:
                  type: string
                occupation:
                  type: string
    """
    data = request.get_json()
    userid = data.get("user_id")
    users_row = databasefunctions.fetch_user_by_id(userid)

    return jsonify(users_row), 200


@app.route("/fetch_favorited_pets", methods=["POST"])
def fetch_favorite_pet():
    """
    fetches all pets favorited by a user 
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
    responses:
      200:
        description: List of favorited pets retrieved successfully.
        schema:
          type: array
          items:
            type: object
            properties:
              pet_id:
                type: integer
              pet_name:
                type: string
              pet_age:
                type: integer
              pet_breed:
                type: string
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
    ---
    responses:
      200:
        description: All users retrieved successfully.
        schema:
          type: array
          items:
            type: object
            properties:
              user_id:
                type: integer
              user_name:
                type: string
              user_age:
                type: integer
              user_location:
                type: string
              user_occupation:
                type: string
    """

    allusers = databasefunctions.fetch_all_users()
    return jsonify(allusers), 200


@app.route("/fetch_allpets", methods=["POST"])
def fetch_allpets():
    """
    fetches all pets in database
    ---
    responses:
      200:
        description: All pets retrieved successfully.
        schema:
          type: array
          items:
            type: object
            properties:
              pet_id:
                type: integer
                example: 102
              name:
                type: string
                example: "Chuck"
              age:
                type: integer
                example: 3
              gender:
                type: string
                example: "Female"
              breed:
                type: string
                example: "Golden Retriever"
              type:
                type: string
                example: "Dog"
              location:
                type: string
                example: "New York"
              photo_path:
                type: string
                example: "images/Chuck.jpg"
    """

    allpets = databasefunctions.fetch_all_pets()
    return jsonify(allpets), 200







if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
