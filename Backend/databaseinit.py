'''ONLY USE THIS IF THE DATABASE IS EMPTY. IT'S THE INIT CODE'''

import sqlite3
from contextlib import closing
import os

def populate_test_data(db_path):
    '''THE ACTUAL FUNCITON'''

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    conn.execute("PRAGMA foreign_keys = ON") 
    # Create tables
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS accounts (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        location TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS pets (
        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT CHECK(gender IN ('male', 'female')),
        breed TEXT,
        type TEXT,
        location TEXT,
        photo_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );


    CREATE TABLE IF NOT EXISTS favorites (
        favorite_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        pet_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    );

    ''')

    # Insert sample users 
    cursor.executescript('''
    INSERT INTO accounts (name, age) VALUES 
    ('Ben Ten', 28),
    ('Spongebob Smith', 35),
    ('Dipper Pines', 25),
    ('Emilia Kirej', 20);
    ''')

    # Insert sample pets
    cursor.executescript('''
    INSERT INTO pets (name, age, gender, breed, type, location, photo_path) VALUES 
    ('Gunner', 9, 'male', 'Golden Retriever', 'dog', 'Myrtle Beach, SC', 'images/gunner.jpg'),
    ('Lizzie Izzie', 5, 'female', 'Donskoy', 'cat', 'Milford, CT', 'images/lizzie_izzie.jpg'),
    ('Chuck', 1, 'male', 'Corgi', 'dog', 'Orlando, FL', 'images/chuck.jpg'),
    ('Monster', 5, 'female', 'Maine Coon', 'cat', 'Houston, TX', 'images/monster.jpg');
    ''')

    # Insert sample favorites
    cursor.executescript('''
    INSERT INTO favorites (user_id, pet_id) VALUES
    (2, 4),
    (1, 2);
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_test_data('Projectdatabase.db')
