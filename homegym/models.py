import sqlite3

    
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create tables
    with open('databases/database.sql', 'r') as f:
        sql = f.read()
        c.executescript(sql)

    conn.commit()
    conn.close()


def clear_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # List of all tables
    tables = ['BadgeType', 'ExercisePlan', 'Exercises', 'FinishTraining', 'Food', 'Friendship', 'Measurements', 'Nutrition', 'TrainingPlan', 'UserBadges', 'Users']

    # Delete all rows from all tables
    for table in tables:
        c.execute(f"DELETE FROM {table}")

    conn.commit()
    conn.close()


def add_user():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Insert a new row of data into the Users table
    c.execute("""
        INSERT INTO Users (Username, Password, Email, BirthDate, RegistrationDate, Role, Status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ('João', 'testpassword', 'testuser@example.com', '2000-01-01', date.today(), 'User', 'Online'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def add_exercises():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Push-ups', 'A basic exercise for upper body strength.', 'https://www.youtube.com/watch?v=euPXf2hqU3s', 'Musculacao', 'Easy');")
    cursor.execute("INSERT INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Sit-ups', 'An exercise for strengthening the abdominal muscles.', 'http://example.com/sit-ups', 'Musculacao', 'Medium');")
    cursor.execute("INSERT INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Squats', 'A lower body exercise targeting the thighs and buttocks.', 'http://example.com/squats', 'Musculacao', 'Hard');")
    cursor.execute("INSERT INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (1, 2, 3);")
    
    db.commit()
    db.close()


def add_plan():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (1, 2, 3);")
    
    db.commit()
    db.close()

