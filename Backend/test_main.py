""" This module contains unit tests for the pet adoption web application, testing the functionality
of various endpoints. It uses the requests library to simulate HTTP requests. """
import requests

def test_get_random_pet():
    """Test for http://localhost:5000/get_random_pet."""
    url = "http://localhost:5000"
    response = requests.get(f"{url}/get_random_pet", timeout=10)
    expected_response = {"id": "9", "name": "Sam", "sex": "Male", "Age": "8",
                         "location": "Connecticut", "Breed": "Pug"}
    assert response.json() == expected_response

def test_add_user_favorite():
    """Test for http://localhost:5000/add_user_favorite."""
    url = "http://localhost:5000"
    favorite_pet1 = {"id": "9", "name": "Sam", "sex": "Male", "Age": "8",
                     "location": "Connecticut", "Breed": "Pug"}
    response = requests.post(f"{url}/add_user_favorite", json=favorite_pet1, timeout=10)
    assert response.json() == [favorite_pet1]
    favorite_pet2 = {"id": "90", "name": "Ben", "sex": "Male", "Age": "2",
                     "location": "New York", "Breed": "Husky"}
    response = requests.post(f"{url}/add_user_favorite", json=favorite_pet2, timeout=10)
    assert response.json() == [favorite_pet1, favorite_pet2]

def test_remove_user_favorite():
    """Test for http://localhost:5000/remove_user_favorite."""
    url = "http://localhost:5000"
    favorite_pet1 = {"id": "9", "name": "Sam", "sex": "Male", "Age": "8",
                     "location": "Connecticut", "Breed": "Pug"}
    response = requests.delete(f"{url}/remove_user_favorite", json=favorite_pet1, timeout=10)
    assert response.json() == []
    favorite_pet2 = {"id": "90", "name": "Ben", "sex": "Male", "Age": "2",
                     "location": "New York", "Breed": "Husky"}
    response = requests.delete(f"{url}/remove_user_favorite", json=favorite_pet2, timeout=10)
    assert response.json() == []

def test_change_user_location():
    """Test for http://localhost:5000/change_user_location."""
    url = "http://localhost:5000"
    response = requests.put(f"{url}/change_user_location", json={"Location": "New York"},
                            timeout=10)
    assert response.json() == {"Location": "New York", "Name": "Eric", "Occupation":
                               "Student", "Password": "2020"}
    