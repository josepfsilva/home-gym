from datetime import date, timedelta
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import sqlite3
from views import mgvideos, mgamificacao, mgamigos, mgtreinos
from models import init_db,clear_db,add_exercises,add_user,add_exercise_plan,add_training_plan,get_username
import secrets
import os


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
   
@app.route('/templates/<path:filename>')
def serve_html(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates'), filename)

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


#paginas base
@app.route("/" , methods=['GET', 'POST'])
def menu():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    username = get_username(session['UserID'])
    
    return render_template('index.html', username = username)

@app.route("/meusplanos" , methods=['GET', 'POST'])
def pagina_planos():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    username = get_username(session['UserID'])
    
    return render_template('MenuPlanos.html', username = username)

@app.route("/meuperfil" , methods=['GET', 'POST'])
def pagina_perfil():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    username = get_username(session['UserID'])
    
    return render_template('Perfil.html', username = username)

@app.route("/novasessao" , methods=['GET', 'POST'])
def pagina_novasessao():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    return render_template('NovaSessao.html')

#fim paginas base





#funções para a API	

@app.route("/planos" , methods=['GET', 'POST'])
def show_all_trainingPlans_from_user():
    #verificar se o user está na sessão
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    userID = session['UserID']
    training_plans_data = {}
    order = {}
    training_plans_ID = mgtreinos.getUserTrainingPlans(userID)

    if training_plans_ID is None:
        return jsonify({'Error': 'No training plans!'}), 404
    
    count = 1
    for id in training_plans_ID:
        if count > 6: #max 6 planos
            break
        id = id[0]
        order[id] = count                                   #{id: order}
        training_plan = mgtreinos.getTrainingPlanData(id)
        training_plans_data[id] = training_plan             #{id: [name, description, type]}
        count += 1
    
    
    combined = [training_plans_data, order]
    print(combined)
    return jsonify(combined),200
    
@app.route("/planosOrder" , methods=['GET', 'POST'])
def planosOrder():

    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    userID = session['UserID']
    order = {}
    training_plans_ID = mgtreinos.getUserTrainingPlans(userID)

    if training_plans_ID is None:
        return jsonify({'Error': 'No training plans!'}), 404
    
    count = 1
    for id in training_plans_ID:
        if count > 6: #max 6 planos
            break
        id = id[0]
        order[count] = id                                   #{id: order}
        count += 1
    
    return jsonify(order),200

@app.route("/planotreino/<trainingPlanID>", methods=['GET', 'POST']) 
def show_trainingPlan(trainingPlanID):
   
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    print(trainingPlanID)
    training_plan_data = mgtreinos.getTrainingPlanData(trainingPlanID)
    print(training_plan_data)
    if training_plan_data is None:
        return jsonify({'Error': 'Training plan not found'}), 404

    
    return jsonify(training_plan_data), 200  


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

    return embed_url




if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
    
    