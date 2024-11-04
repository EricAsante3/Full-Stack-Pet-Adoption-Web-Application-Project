from contextlib import closing
import sqlite3

def connect_db():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('/home/sus98/2102/proj/cse2102-fall24-Team51/Backend/testData.db') #this might change

def insert_user(name, age, marital_status, pet_preference):
    """Insert a new user into the users table."""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO users (name, age, marital_status, pet_preference)
               VALUES (?, ?, ?, ?)''',
            (name, age, marital_status, pet_preference)
        )
        conn.commit()
        return cursor.lastrowid

def insert_pet(name, age, gender, breed, type, location, picture=None):
    """Insert a new pet into the pets table."""
    with closing(connect_db()) as conn, conn:
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO pets (name, age, gender, breed, type, location, picture)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (name, age, gender, breed, type, location, picture)
        )
        conn.commit()
        return cursor.lastrowid

def fetch_all_pets():
    """Retrieve all pets from the pets table."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pets")
        return cursor.fetchall()

def fetch_user_by_id(user_id):
    """Retrieve a user by their user_id."""
    with closing(connect_db()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone()
