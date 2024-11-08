'''INIT TABLES IN DATABASE'''

import sqlite3

def create_database_tabels(db_path):
    '''THE ACTUAL FUNCITON'''

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    conn.execute("PRAGMA foreign_keys = ON")
    # Create tables
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS accounts (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
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


    INSERT INTO pets (name, age, gender, breed, type, location, photo_path)
    VALUES 
    ('Bella', 3, 'female', 'Golden Retriever', 'dog', 'New York', 'images/Chuck.jpg'),
    ('Max', 5, 'male', 'Maine Coon', 'cat', 'Boston', 'images/gunner.jpg'),
    ('Luna', 2, 'female', 'Siamese', 'cat', 'Chicago', 'images/luna.jpg'),
    ('Charlie', 4, 'male', 'Beagle', 'dog', 'Los Angeles', 'images/lizzie_izzie.jpg'),
    ('Daisy', 1, 'female', 'Labrador Retriever', 'dog', 'Miami', 'images/monster.jpg');


    ''')


    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database_tabels('projectdatabase.db')
