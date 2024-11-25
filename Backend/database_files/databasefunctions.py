'''DATABASE FUNCTIONS'''
from contextlib import closing
import sqlite3

def connect_db():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('projectdatabase.db') #this might change

# --------------------- insert functions

def insert_user(username, password, first_name, last_name):
    """Insert a new user into the accounts table."""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute('''SELECT COUNT(*) FROM accounts WHERE username = ?''', (username,))
        user_exists = cursor.fetchone()[0]
        
        if user_exists > 0:
            # If the username already exists, return None or an error message
            return None  # or return some error message or status
        
        cursor.execute(
            '''INSERT INTO accounts (username, password, first_name, last_name)
               VALUES (?, ?, ?, ?)''',
            (username, password, first_name, last_name)
        )
        conn.commit()
        return cursor.lastrowid


def insert_pet(name, age, gender, type, location, photo_path=None, breed=None, paragraph=None):
    """Insert a new pet into the pets table."""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO pets (name, age, gender, type, location, photo_path, breed, paragraph)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (name, age, gender, type, location, photo_path, breed, paragraph)
        )
        conn.commit()
        return cursor.lastrowid


def insert_favorite(user_id, pet_id):
    """Insert usere favorite pet into favorites table"""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO favorites (user_id, pet_id)
               VALUES (?, ?)''',
            (user_id, pet_id)
        )
        conn.commit()
        return cursor.lastrowid

# ---------------------------remove functions

def remove_user(user_id):
    """Remove a pet from the accounts table."""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()
        cursor.execute(
            '''DELETE FROM accounts
               WHERE user_id = ?''',
            (user_id,)
        )
        conn.commit()
        return cursor.rowcount


def remove_pet(pet_id):
    """Remove a pet from the pets table."""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()
        cursor.execute(
            '''DELETE FROM pets
               WHERE pet_id = ?''',
            (pet_id,)
        )
        conn.commit()
        return cursor.rowcount


def remove_favorite(user_id, pet_id):
    """Remove a favorite row from the favorites table based on user_id and pet_id."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()

        # Execute DELETE query to remove the row matching user_id and pet_id
        cursor.execute("""
            DELETE FROM favorites
            WHERE user_id = ? AND pet_id = ?
        """, (user_id, pet_id))

        conn.commit()
        return cursor.rowcount  # Returns the number of rows affected (should be 1 if successful)

# ------------------------------------------- change fucntions


def change_user_attributes(user_id, attribute, change):
    """Update a user's attribute in the accounts table."""

    # List of valid column names to avoid SQL injection
    valid_columns = ['name', 'age', 'location', 'password']  # Add your valid column names here

    if attribute not in valid_columns:
        raise ValueError("Invalid attribute name.")

    with closing(connect_db()) as conn:
        cursor = conn.cursor()

        # Use the attribute directly, now it's safe since we validated it
        cursor.execute(f"""
            UPDATE accounts
            SET {attribute} = ?
            WHERE user_id = ?
        """, (change, user_id))

        conn.commit()
        return fetch_user_by_id(user_id)


def change_pet_attributes(pet_id, attribute, change):
    """Update a user's attribute in the accounts table."""

    # List of valid column names to avoid SQL injection
    valid_columns = ['name', 'age', 'location', 'breed',
                     'gender', 'type', 'photo_path']  # Add your valid column names here

    if attribute not in valid_columns:
        raise ValueError("Invalid attribute name.")

    with closing(connect_db()) as conn:
        cursor = conn.cursor()

        # Use the attribute directly, now it's safe since we validated it
        cursor.execute(f"""
            UPDATE pets
            SET {attribute} = ?
            WHERE pet_id = ?
        """, (change, pet_id))

        conn.commit()
        return fetch_pet_by_id(pet_id)

# ------------------------------------- fetch functions


def fetch_userid_from_username_and_password(username,password):
    """Get a users ID from there username and password"""

    with closing(connect_db()) as conn:
        cursor = conn.cursor()

        # Execute DELETE query to remove the row matching user_id and pet_id
        cursor.execute("""
            SELECT user_id FROM accounts
            WHERE username = ? AND password = ?
        """, (username, password))

        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None


def fetch_favorites_by_user(user_id):
    """Fetch all favorite pets for a given user_id."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT pets.*
            FROM pets
            INNER JOIN favorites ON pets.pet_id = favorites.pet_id
            WHERE favorites.user_id = ?
        """, (user_id,))

        return cursor.fetchall()


def fetch_all_users():
    """Retrieve all users from the accounts table."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts")
        return cursor.fetchall()


def fetch_all_pets():
    """Retrieve all pets from the pets table."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pets")
        return cursor.fetchall()


def fetch_user_by_id(user_id):
    """Retrieve a user by their account_id."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE user_id = ?", (user_id,))
        return cursor.fetchone()


def fetch_pet_by_id(pet_id):
    """Retrieve a pet by their pet_id."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pets WHERE pet_id = ?", (pet_id,))
        return cursor.fetchone()


# -------------------------------------------------------------
