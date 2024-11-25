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
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS pets (
        pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT CHECK(gender IN ('Male', 'Female')),
        type TEXT,
        location TEXT,
        photo_path TEXT,
        breed TEXT,
        paragraph TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );


    CREATE TABLE favorites (
        favorite_id_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        pet_id INTEGER NOT NULL,
        UNIQUE(user_id, pet_id)
    );


    INSERT INTO pets (name, age, gender, type, location, photo_path, breed, paragraph)
    VALUES      
    ("Bella", 2, "Female", "Dog", "New York, NY", "/assets/images/Bella.jpg", "Labrador Retriever", "Bella is a sweet Labrador Retriever who loves long walks in the park and cuddles on the couch."),
    ("Max", 3, "Male", "Cat", "Los Angeles, CA", "/assets/images/Max.jpg", "Siamese", "Max is a curious Siamese cat who enjoys lounging in sunny spots and chasing laser pointers."),
    ("Luna", 1, "Female", "Dog", "Austin, TX", "/assets/images/Luna.jpg", "Golden Retriever", "Luna is a playful Golden Retriever pup who loves fetching tennis balls and meeting new friends."),
    ("Charlie", 4, "Male", "Cat", "Seattle, WA", "/assets/images/Charlie.jpg", "Maine Coon", "Charlie is a gentle Maine Coon with a fluffy coat and a love for snuggling."),
    ("Lancy", 5, "Male", "Dog", "Chicago, IL", "/assets/images/Lucy.jpg", "Beagle", "Lucy is an energetic Beagle who loves exploring trails and sniffing out new scents."),
    ("Milo", 1, "Male", "Dog", "Houston, TX", "/assets/images/Milo.jpg", "Poodle", "Milo is an intelligent Poodle with a knack for learning tricks and making people smile."),
    ("Sadie", 2, "Female", "Cat", "Phoenix, AZ", "/assets/images/Sadie.jpg", "Bengal", "Sadie is an active Bengal cat who loves climbing and playing with her favorite toys."),
    ("Rocky", 6, "Male", "Dog", "Miami, FL", "/assets/images/Rocky.jpg", "Bulldog", "Rocky is a laid-back Bulldog who enjoys relaxing and spending time with his family."),
    ("Chloe", 1, "Female", "Dog", "Dallas, TX", "/assets/images/Chloe.jpg", "Dachshund", "Chloe is a spunky Dachshund who loves burrowing under blankets and going on small adventures."),
    ("Jack", 7, "Male", "Cat", "Boston, MA", "/assets/images/Jack.jpg", "Persian", "Jack is a dignified Persian cat with a luxurious coat and a calm demeanor."),
    ("Oliver", 1, "Male", "Dog", "Orlando, FL", "/assets/images/Oliver.jpg", "Corgi", "Oliver is a cheerful Corgi with a love for belly rubs and herding anything that moves."),
    ("Toby", 3, "Male", "Dog", "Salt Lake City, UT", "/assets/images/Toby.jpg", "Australian Shepherd", "Toby is a hardworking Australian Shepherd who loves running and solving puzzles."),
    ("Lily", 2, "Female", "Cat", "Sacramento, CA", "/assets/images/Lily.jpg", "Ragdoll", "Lily is a calm Ragdoll cat who adores being pampered and spending time with her favorite humans."),
    ("Zoe", 6, "Female", "Dog", "Raleigh, NC", "/assets/images/Zoe.jpg", "Boxer", "Zoe is a spirited Boxer with boundless energy and a love for outdoor play.");
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database_tabels('projectdatabase.db')
