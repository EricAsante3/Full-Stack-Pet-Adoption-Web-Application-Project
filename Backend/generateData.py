'''ONLY USE THIS IF THE DATABASE IS EMPTY. IT'S THE INIT CODE'''

import sqlite3
from contextlib import closing
import os



def populate_test_data(db_path):
    '''THE ACTUAL FUNCITON'''

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()



    # Create tables
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marital_status TEXT,
        pet_preference TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS pets (
        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT CHECK(gender IN ('male', 'female')),
        breed TEXT,
        type TEXT CHECK(type IN ('dog', 'cat')),
        location TEXT,
        photo_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS user_tests (
        test_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question TEXT,
        answer TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    ''') #ur welcome :)


    # Insert sample users 
    cursor.executescript('''
    INSERT INTO users (name, age, marital_status, pet_preference) VALUES 
    ('Ben Ten', 28, 'single', 'dog'),
    ('Spongebob Smith', 35, 'married', 'cat'),
    ('Dipper Pines', 25, 'married', 'any'),
    ('Emilia Kirej', 20, 'married', 'dog');
                         
    ''')
                         
    # Insert sample pets
    cursor.executescript('''
    INSERT INTO pets (name, age, gender, breed, type, location, photo_path) VALUES 
    ('Gunner', 9, 'male', 'Golden Retriever', 'dog', 'Myrtle Beach, SC', 'images/gunner.jpg'),
    ('Lizzie Izzie', 5, 'female', 'Donskoy', 'cat', 'Milford, CT', 'images/lizzie_izzie.jpg'),
    ('Chuck', 1, 'male', 'Corgi', 'dog', 'Orlando, FL', 'images/chuck.jpg'),
    ('Monster', 5, 'female', 'Maine Coon', 'cat', 'Houston, TX', 'images/monster.jpg');
    ''')

    conn.commit()
    conn.close()




#populate_test_data('/home/sus98/2102/proj/cse2102-fall24-Team51/Backend/testData.db')


