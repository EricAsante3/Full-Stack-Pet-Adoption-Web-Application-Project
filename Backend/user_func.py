""" This module handles user-related functionalities such as 
managing favorites and updating user information. """

user_favorite_database = []  # Simulate a database for user favorites
user_acc_info = {
    "Name": "Eric",
    "Password": "2020",
    "Location": "Connecticut",
    "Occupation": "Student"
}

def add_user_favorite(json_data):
    """Add user favorite pet to the database."""
    user_favorite_database.append(json_data)
    return user_favorite_database  # Return updated user favorites database

def remove_user_favorite(json_data):
    """Remove user favorite pet from the database."""
    user_favorite_database.remove(json_data)
    return user_favorite_database  # Return updated user favorites database

def replace_user_location(new_location):
    """Change the user account location."""
    new_location = new_location.get("Location")
    user_acc_info["Location"] = new_location  # Set new location associated with the user
    return user_acc_info  # Return updated user account information
