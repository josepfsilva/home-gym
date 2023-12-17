from datetime import date
from flask import Flask, render_template
import sqlite3
from views import mgvideos, mgamificacao, mgamigos, mgtreinos
from models import init_db,clear_db

app = Flask(__name__)
#app.config.from_object('config.py')

def add_exercises():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Push-ups', 'A basic exercise for upper body strength.', 'http://example.com/push-ups', 'Musculacao', 'Easy');")
    cursor.execute("INSERT INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Sit-ups', 'An exercise for strengthening the abdominal muscles.', 'http://example.com/sit-ups', 'Musculacao', 'Medium');")
    cursor.execute("INSERT INTO Exercises (Name, Description, URL, Type, Difficulty) VALUES ('Squats', 'A lower body exercise targeting the thighs and buttocks.', 'http://example.com/squats', 'Musculacao', 'Hard');")
    cursor.execute("INSERT INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (1, 2, 3);")
    
    db.commit()
    db.close()




with app.app_context():
    init_db()
    #clear_db()
    add_exercises()

    
    



@app.route("/" , methods=['GET', 'POST'])
def open():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)