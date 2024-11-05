"""
This module provides functions for HTTP communication and 
route functions
"""
UserFaviorteDataBase = [] # pretend this is a database

UserAccInfo = {"Name":"eric",
               "Password":"2020", 
               "Location":"connecticut",
               "Occupation":"Student"} # example user information

# add user faviorte pet to database
def add_user_faviorte(jsondata):
    """
    add user to database and return database elements
    """
    UserFaviorteDataBase.append(jsondata)
    # accesses database and append post json in database
    return UserFaviorteDataBase # return new user database


# Remove user faviorte pet to database
def remove_user_faviorte(jsondata):
    """
    remove user from database and return database elements
    """
    UserFaviorteDataBase.remove(jsondata)
    # accesses database and append post json in database
    return UserFaviorteDataBase # return new user database


# Change a Users account location
def replace_user_location(newlocation):
    """
    Replace location associated with a user account
    """
    newlocation = newlocation.get('Location')
    UserAccInfo["Location"] = newlocation # Set location accosiated with user to new location
    return UserAccInfo # retrun user account info
