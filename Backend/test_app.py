"""
Pytest for fake API
"""
import requests

UNIQUE_USER_ID = None
UNIQUE_PET_ID = None


def test_insert_user():
    """
    Test for http://localhost:5000/add_newuser, adding user to database
    """
    global UNIQUE_USER_ID
    url = "http://localhost:5000"

    UNIQUE_USER_ID = requests.post((url + "/add_newuser"),
                                   json={"username":"sam2213",
                                        "password":"catlover20","name": "sam",
                                        "age": 17,  "location": "jamaica"},timeout=10)

    response1 = requests.post((url + "/fetch_user"),json=UNIQUE_USER_ID.json(), timeout=10)
    response2 = requests.post((url + "/fetch_allusers"), timeout=10)

    assert (response1.json() in response2.json()) is True


def test_insert_pet():
    """
    Test for http://localhost:5000/add_newpet, adding new pet to database to database
    """
    global UNIQUE_PET_ID
    url = "http://localhost:5000"
    UNIQUE_PET_ID = requests.post((url + "/add_newpet"),
                                  json={"name": "sam", "age": 17,
                                        "gender":"female","breed":"pug",
                                        "type":"cat","location": "jamaica",
                                        "photo_path":"images/sam.jpg"},timeout=10) 

    response1 = requests.post((url + "/fetch_pet"),json=UNIQUE_PET_ID.json(), timeout=10)
    response2 = requests.post((url + "/fetch_allpets"), timeout=10)

    assert (response1.json() in response2.json()) is True

def test_insert_favorite_relation():
    """
    Test for http://localhost:5000/add_newfavorite, adding users favorited pet into the database
    """
    global UNIQUE_USER_ID
    global UNIQUE_PET_ID

    url = "http://localhost:5000"


    requests.post((url + "/add_newfavorite"),
                  json={"user_id": UNIQUE_USER_ID.json().get("user_id"),
                        "pet_id": UNIQUE_PET_ID.json().get("pet_id")},timeout=10)

    response1 = requests.post((url + "/fetch_pet"),json=UNIQUE_PET_ID.json(), timeout=10)
    response2 = requests.post((url + "/fetch_favorited_pets"),json=UNIQUE_USER_ID.json(),timeout=10)

    assert (response1.json() in response2.json()) is True


# -----------------------------------------------------------------------------

def test_fetch_userid():
    """
    Test for http://localhost:5000/fetch_userid, 
    retrieve userid accosiated with username and password
    """

    global UNIQUE_USER_ID
    global UNIQUE_PET_ID

    url = "http://localhost:5000"
    userid = requests.post((url + "/fetch_userid"),
                           json={"username": "sam2213",
                                 "password": "catlover20"}, timeout=10)

    assert userid.json() == UNIQUE_USER_ID.json().get("user_id")

# ----------------------------------------------------------------------------------

def test_remove_favorite_relation():
    """
    Test for http://localhost:5000/remove_favorite, remove users favorited pet from the database
    """

    global UNIQUE_USER_ID
    global UNIQUE_PET_ID

    url = "http://localhost:5000"

    requests.delete((url + "/remove_favorite"),
                    json={"user_id": UNIQUE_USER_ID.json().get("user_id"),
                          "pet_id": UNIQUE_PET_ID.json().get("pet_id")},timeout=10)


    response = requests.post((url + "/fetch_favorited_pets"),json=UNIQUE_USER_ID.json(),timeout=10)

    assert (response.json()) == []


def test_remove_user():
    """
    Test for http://localhost:5000/remove_user
    """

    global UNIQUE_USER_ID
    global UNIQUE_PET_ID

    url = "http://localhost:5000"

    requests.delete((url + "/remove_user"), json=UNIQUE_USER_ID.json(), timeout=10)

    response = requests.post((url + "/fetch_user"),json=UNIQUE_USER_ID.json(), timeout=10)

    assert response.json() is None


def test_remove_pet():
    """
    Test for http://localhost:5000/remove_pet
    """

    url = "http://localhost:5000"

    requests.delete((url + "/remove_pet"), json=UNIQUE_PET_ID.json(), timeout=10)

    response = requests.post((url + "/fetch_pet"),json=UNIQUE_PET_ID.json(), timeout=10)

    assert response.json() is None
