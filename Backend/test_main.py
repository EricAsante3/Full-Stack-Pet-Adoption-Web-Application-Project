import requests
from flask import Flask, json, request, jsonify

def test_Get_Random_pet():
    """
    Test for http://localhost:5000/Get_Random_pet
    """

    url = "http://localhost:5000"

    response = requests.get(url + "/Get_Random_pet")

    expected_response = {
        "id": "9",
        "name": "sam",
        "sex": "male",
        "Age": "8",
        "location": "Connecticwut",
        "Breed": "Pug"
    }

    assert response.json() == expected_response

# -----------------------------------------------------------------------------

def test_Add_User_Faviorte():
    """
    Test for http://localhost:5000/Add_User_Faviorte
    """

    url = "http://localhost:5000"

    FaviortePet1 = {
        "id": "9",
        "name": "sam",
        "sex": "male",
        "Age": "8",
        "location": "Connecticut",
        "Breed": "Pug"
    }


    response = requests.post((url + "/Add_User_Faviorte"), json=(FaviortePet1))

    assert response.json() == [{'Age': '8', 'Breed': 'Pug', 'id': '9', 'location': 'Connecticut', 'name': 'sam', 'sex': 'male'}]

    FaviortePet2 = {
        "id": "90",
        "name": "ben",
        "sex": "male",
        "Age": "2",
        "location": "New York",
        "Breed": "Husky"
    }

    response = requests.post((url + "/Add_User_Faviorte"), json=(FaviortePet2))

    assert response.json() == [{'Age': '8', 'Breed': 'Pug', 'id': '9', 'location': 'Connecticut', 'name': 'sam', 'sex': 'male'}, {'Age': '2', 'Breed': 'Husky', 'id': '90'
, 'location': 'New York', 'name': 'ben', 'sex': 'male'}]

# ----------------------------------------------------------------------------------

def test_Remove_User_Faviorte():
    """
    Test for http://localhost:5000/Remove_User_Faviorte
    """

    url = "http://localhost:5000"

    FaviortePet1 = {
        "id": "9",
        "name": "sam",
        "sex": "male",
        "Age": "8",
        "location": "Connecticut",
        "Breed": "Pug"
    }


    response = requests.delete((url + "/Remove_User_Faviorte"), json=(FaviortePet1))

    assert response.json() == [{'Age': '2', 'Breed': 'Husky', 'id': '90', 'location': 'New York', 'name': 'ben', 'sex': 'male'}]

    FaviortePet2 = {
        "id": "90",
        "name": "ben",
        "sex": "male",
        "Age": "2",
        "location": "New York",
        "Breed": "Husky"
    }

    response = requests.delete((url + "/Remove_User_Faviorte"), json=(FaviortePet2))

    assert response.json() == []
# ----------------------------------------------------------------------------------



def test_Change_User_Location():
    """
    Test for http://localhost:5000/Change_User_Location
    """

    url = "http://localhost:5000"

    response = requests.put((url + "/Change_User_Location"), json={"Location":"New York"})

    assert response.json() == {"Location": "New York","Name": "eric","Occupation": "Student","Password": "2020"}


    response = requests.put((url + "/Change_User_Location"), json={"Location":"Chicago"})

    assert response.json() == {"Location": "Chicago","Name": "eric","Occupation": "Student","Password": "2020"}

    response = requests.put((url + "/Change_User_Location"), json={"Location":"Massachusetts"})

    assert response.json() == {"Location": "Massachusetts","Name": "eric","Occupation": "Student","Password": "2020"}









test_Get_Random_pet()
test_Add_User_Faviorte()
test_Remove_User_Faviorte()
test_Change_User_Location()
print("Test check Complete: Passed")
