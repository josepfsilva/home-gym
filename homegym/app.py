from datetime import date, timedelta
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from views import mgvideos, mgamificacao, mgamigos, mgtreinos
from models import init_db,clear_db,add_exercises,add_user,add_exercise_plan,add_training_plan
import secrets

app = Flask(__name__)
#app.config.from_object('config.py')

app.secret_key = secrets.token_hex(32) #chave para a sessão

with app.app_context():
    init_db()
    #clear_db()
    add_exercises()
    add_user()
    add_exercise_plan()
    add_training_plan()
   

@app.route('/login', methods=['GET', 'POST'])
def login():

    if 'UserID' in session:
        session.pop('UserID')
        return redirect('/login')


    if(request.method == 'POST'):

        username = request.form.get('Username')
        password = request.form.get('Password')

        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("SELECT UserId FROM Users WHERE Username = ? and Password = ?", (username, password))

        validLogin = cursor.fetchone()
        cursor.close()
        db.close()

        if(validLogin == None):
            return render_template('login.html')

        if  validLogin[0]:
            session['UserID'] = validLogin[0]
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=20)   #tempo da sessão ativa
            return redirect('/')

    return render_template('login.html')



@app.route("/" , methods=['GET', 'POST'])
def menu():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    return render_template('index.html')



@app.route("/planos" , methods=['GET', 'POST'])
def show_all_trainingPlans_from_user():
    #verificar se o user está na sessão
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    userID = session['UserID']
    training_plans_data = {}
    training_plans_ID = mgtreinos.getUserTrainingPlans(userID)

    for id in training_plans_ID:
        id = id[0]
        training_plan = mgtreinos.getTrainingPlanData(id)
        training_plans_data[id] = training_plan              #{id: [name, description, type]}

    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT Username
                   FROM Users
                   where UserID = ?
                   """,(userID,))
    username = cursor.fetchone()[0]
    db.close()
    
    return render_template('MenuPlanos.html', training_plans_data = training_plans_data, username = username)
    

@app.route("/planos/<int:trainingPlanID>", methods=['GET', 'POST'])
def show_trainingPlan(trainingPlanID):
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    training_plan_data = mgtreinos.getTrainingPlanData(trainingPlanID)
    print(training_plan_data)
    
    return render_template('menuPlanos.html', training_plan_data = training_plan_data)


@app.route("/exercise", methods=['GET', 'POST'])
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
    
    