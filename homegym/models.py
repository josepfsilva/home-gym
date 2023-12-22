import sqlite3
from datetime import date
from flask import Flask

    
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

    # INSERT OR IGNORE a new row of data into the Users table
    c.execute("""
        INSERT OR IGNORE INTO Users (Username, Password, Email, BirthDate, RegistrationDate, Role, Status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ('Maria', '1234', 'testuser@example.com', '1960-01-01', date.today(), 'User', 'Online'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def add_exercises():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    #upper body
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Flexões', 'Um exercício de corpo inteiro que trabalha o peito, ombros e tríceps.', 'http://example.com/push-ups', 'Musculacao', 'Medio');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Flexões em diamante', 'Um exercício de corpo inteiro que trabalha o peito, ombros e tríceps.', 'http://example.com/diamond-push-ups', 'Musculacao', 'Dificil');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Abdominais', 'Um exercício de corpo inteiro que trabalha o core.', 'http://example.com/crunches', 'Musculacao', 'Facil');")
    
    #lower body
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Agachamentos', 'Um exercício composto que trabalha os quadríceps, isquiotibiais e glúteos.', 'http://example.com/squats', 'Musculacao', 'Medio');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Lunges', 'Um exercício de perna que trabalha os quadríceps e glúteos.', 'http://example.com/lunges', 'Musculacao', 'Facil');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Agachamentos com salto', 'Um exercício de perna que trabalha os quadríceps e glúteos.', 'http://example.com/jump-squats', 'Musculacao', 'Dificil');")
    
    #cardio
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Polichinelos', 'Um exercício de cardio de corpo inteiro que pode ser feito em casa.', 'http://example.com/jumping-jacks', 'Cardio', 'Facil');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Burpees', 'Um exercício de cardio de corpo inteiro que combina agachamentos, saltos e flexões.', 'http://example.com/burpees', 'Cardio', 'Dificil');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Mountain Climbers', 'Um exercício de cardio que também trabalha o core.', 'http://example.com/mountain-climbers', 'Cardio', 'Medio');")
        
    db.commit()
    db.close()


def add_exercise_plan():    
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (1, 2, 3);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (4, 5, 6);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (7, 8, 9);")
    
    
    db.commit()
    db.close()

def add_training_plan():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, ExercisePlanID, UserID) VALUES ('Treino de parte superior', 'Treino de ombros', 'Musculacao', 1, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, ExercisePlanID, UserID) VALUES ('Treino de parte inferior', 'Treino de pernas', 'Musculacao', 2, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, ExercisePlanID, UserID) VALUES ('Treino de cardio', 'Treino de cardio', 'Cardio', 3, 1);")
    
    db.commit()
    db.close()

def get_username(userID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT Username FROM Users WHERE UserID = ?", (userID,))
    username = cursor.fetchone()
    db.close()
    return username[0]