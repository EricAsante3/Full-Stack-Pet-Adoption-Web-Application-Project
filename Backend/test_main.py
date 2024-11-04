"""
Pytest for fake API
"""

import requests

def test_get_random_pet():
    """
    Test for http://localhost:5000/Get_Random_pet
    """

    url = "http://localhost:5000"

    response = requests.get((url + "/Get_Random_pet"), timeout=10)

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

def test_add_user_faviorte():
    """
    Test for http://localhost:5000/Add_User_Faviorte
    """

    url = "http://localhost:5000"

    faviortepet1 = {
        "id": "9",
        "name": "sam",
        "sex": "male",
        "Age": "8",
        "location": "Connecticut",
        "Breed": "Pug"
    }


    response = requests.post((url + "/Add_User_Faviorte"), json=faviortepet1, timeout=10)

    assert response.json() == [{'Age': '8',
                                'Breed': 'Pug',
                                'id': '9',
                                'location':
                                'Connecticut',
                                'name': 'sam',
                                'sex': 'male'}]

    faviortepet2 = {
        "id": "90",
        "name": "ben",
        "sex": "male",
        "Age": "2",
        "location": "New York",
        "Breed": "Husky"
    }

    response = requests.post((url + "/Add_User_Faviorte"), json=faviortepet2, timeout=10)

    assert response.json() == [{'Age': '8',
                                'Breed': 'Pug',
                                'id': '9',
                                'location': 'Connecticut',
                                'name': 'sam',
                                'sex': 'male'}, 
                                {'Age': '2',
                                 'Breed': 'Husky',
                                 'id': '90',
                                 'location': 'New York',
                                 'name': 'ben',
                                 'sex': 'male'}]

# ----------------------------------------------------------------------------------

def test_remove_user_faviorte():
    """
    Test for http://localhost:5000/Remove_User_Faviorte
    """

    url = "http://localhost:5000"

    faviortepet1 = {
        "id": "9",
        "name": "sam",
        "sex": "male",
        "Age": "8",
        "location": "Connecticut",
        "Breed": "Pug"
    }


    response = requests.delete((url + "/Remove_User_Faviorte"), json=faviortepet1, timeout=10)

    assert response.json() == [{'Age': '2',
                                'Breed': 'Husky',
                                'id': '90',
                                'location': 'New York',
                                'name': 'ben',
                                'sex': 'male'}]

    faviortepet2 = {
        "id": "90",
        "name": "ben",
        "sex": "male",
        "Age": "2",
        "location": "New York",
        "Breed": "Husky"
    }

    response = requests.delete((url + "/Remove_User_Faviorte"), json=faviortepet2, timeout=10)

    assert response.json() == []
# ----------------------------------------------------------------------------------



def test_change_user_location():
    """
    Test for http://localhost:5000/Change_User_Location
    """

    url = "http://localhost:5000"

    response = requests.put((url + "/Change_User_Location"),
                             json={"Location":"New York"},
                             timeout=10)

    assert response.json() == {"Location": "New York",
                               "Name": "eric",
                               "Occupation": "Student",
                               "Password": "2020"}


    response = requests.put((url + "/Change_User_Location"),
                             json={"Location":"Chicago"},
                             timeout=10)

    assert response.json() == {"Location": "Chicago",
                               "Name": "eric",
                               "Occupation": "Student",
                               "Password": "2020"}

    response = requests.put((url + "/Change_User_Location"),
                             json={"Location":"Massachusetts"},
                             timeout=10)

    assert response.json() == {"Location": "Massachusetts",
                               "Name": "eric",
                               "Occupation": "Student",
                               "Password": "2020"}
