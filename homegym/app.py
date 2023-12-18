from datetime import date
from flask import Flask, render_template
import sqlite3
from views import mgvideos, mgamificacao, mgamigos, mgtreinos
from models import init_db,clear_db

app = Flask(__name__)
#app.config.from_object('config.py')


def add_user():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Insert a new row of data into the Users table
    c.execute("""
        INSERT OR IGNORE INTO Users (Username, Password, Email, BirthDate, RegistrationDate, Role, Status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ('João', 'testpassword', 'testuser@example.com', '2000-01-01', date.today(), 'User', 'Online'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def add_exercises():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Push-ups', 'A basic exercise for upper body strength.', 'https://www.youtube.com/watch?v=euPXf2hqU3s', 'Musculacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Sit-ups', 'An exercise for strengthening the abdominal muscles.', 'http://example.com/sit-ups', 'Musculacao', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Squats', 'A lower body exercise targeting the thighs and buttocks.', 'http://example.com/squats', 'Musculacao', 'Hard');")
    
    db.commit()
    db.close()

def add_plan():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (1, 2, 3);")
    
    db.commit()
    db.close()




with app.app_context():
    init_db()
    #clear_db()
    add_exercises()
    add_user()
    add_plan()
    

    
    



@app.route("/" , methods=['GET', 'POST'])
def open():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT Username
                   FROM Users
                   where UserID = 1
                   """)
    user = cursor.fetchone()[0]
    db.close()
    
    
    
    db = sqlite3.connect('database.db')
    cursor = db.cursor() 
    cursor.execute( """
            SELECT e1.Name, e1.Description,e1.Type,e1.Difficulty,
                   e2.Name, e2.Description,e2.Type,e2.Difficulty,
                   e3.Name, e3.Description,e3.Type,e3.Difficulty
            FROM ExercisePlan
            INNER JOIN Exercises e1 ON ExercisePlan.Exercise1 = e1.ExerciseID
            INNER JOIN Exercises e2 ON ExercisePlan.Exercise2 = e2.ExerciseID
            INNER JOIN Exercises e3 ON ExercisePlan.Exercise3 = e3.ExerciseID
            WHERE ExercisePlan.ExercisePlanID = 1
                    """)
    
    exercise_data = cursor.fetchone()
    db.close()
    
    exercises = [exercise_data[i:i+4] for i in range(0,len(exercise_data),4)]
    
    return render_template('index.html', exercises = exercises, user = user)
    
def convert_to_embed_url(url):
    video_id = url.split('v=')[1]
    embed_url = 'https://www.youtube.com/embed/' + video_id
    return embed_url

@app.route("/exercise")
def exercise():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("""
        SELECT URL
        FROM Exercises
        WHERE ExerciseID = 1;
    """,)

    url = cursor.fetchone()[0]
    embed_url = convert_to_embed_url(url)
    db.close()

    return render_template('exercise.html', url=embed_url)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
    
    