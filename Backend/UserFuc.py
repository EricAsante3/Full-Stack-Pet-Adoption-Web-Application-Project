from flask import Flask, request, json, jsonify

UserFaviorteDataBase = [] # pretend this is a database

UserAccInfo = {"Name":"eric","Password":"2020", "Location":"connecticut","Occupation":"Student"} # example user information

# add user faviorte pet to database
def Add_User_Faviorte(jsondata):
    UserFaviorteDataBase.append(jsondata)

    # accesses database and append post json in database
    return UserFaviorteDataBase # return new user database


# Remove user faviorte pet to database
def Remove_User_Faviorte(jsondata):
    UserFaviorteDataBase.remove(jsondata)

    # accesses database and append post json in database
    return UserFaviorteDataBase # return new user database


# Change a Users account location
def Replace_User_Location(NewLocation):
    NewLocation = NewLocation.get('Location') 

    UserAccInfo["Location"] = NewLocation # Set location accosiated with user to new location 
    return UserAccInfo # retrun user account info
