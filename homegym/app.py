from datetime import date
from flask import Flask, render_template
import sqlite3
from views import mgvideos, mgamificacao, mgamigos, mgtreinos
from models import init_db,clear_db,add_exercises,add_user,add_plan

app = Flask(__name__)
#app.config.from_object('config.py')


with app.app_context():
    init_db()
    #clear_db()
    add_exercises()
    add_user()
    add_plan()
   
 

@app.route("/" , methods=['GET', 'POST'])
def menu():

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
    embed_url = mgvideos.convert_to_embed_url(url)
    db.close()

    return render_template('exercise.html', url=embed_url)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
    
    