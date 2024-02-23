from datetime import date, timedelta, datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import sqlite3
from views import mgvideos, mgamificacao, mgamigos, mgtreinos
from models import init_db,clear_db,add_exercises,add_user,add_exercise_plan,add_training_plan,get_username,get_user_data,get_age, add_badge_types, add_user_badges
import secrets
import os


app = Flask(__name__)
#app.config.from_object('config.py')

app.secret_key = secrets.token_hex(32) #chave para a sessão

with app.app_context():
    init_db()
    clear_db()
    add_exercises()
    add_user()
    add_badge_types()
    add_exercise_plan()
    add_training_plan()
    add_user_badges()
   
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
    image_path = get_user_data(session['UserID'])[5]
    
    return render_template('index.html', username = username, image_path = image_path)

@app.route("/meusplanos" , methods=['GET', 'POST'])
def pagina_planos():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    username = get_username(session['UserID'])
    image_path = get_user_data(session['UserID'])[5]
    
    return render_template('MenuPlanos.html', username = username, image_path = image_path)

@app.route("/meuperfil" , methods=['GET', 'POST'])
def pagina_perfil():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    username = get_username(session['UserID'])
    name = get_user_data(session['UserID'])[3]
    surname = get_user_data(session['UserID'])[4]
    
    birthday_user = get_user_data(session['UserID'])[9]
    birthday_data = datetime.strptime( birthday_user, "%Y-%m-%d")
    birthday = birthday_data.strftime("%d-%m-%Y")# Formata a data no estilo europeu
    age = get_age(birthday_data)
    height = get_user_data(session['UserID'])[7]
    weight = get_user_data(session['UserID'])[6]

    time = datetime.now().strftime('%H:%M')  # Formata a hora para mostrar apenas horas e minutos
    date_today = date.today().strftime('%d/%m/%Y')  
    
    image_path = get_user_data(session['UserID'])[5]
    
    
    badge_id = mgamificacao.getbadges_type(session['UserID'])
    badge_data_list = [mgamificacao.getbadges_data(id[0]) for id in badge_id]
    badge_images = [data[3] for data in badge_data_list]
    

    return render_template('Perfil.html', username = username, name=name, surname=surname, birthday = birthday, time = time, date_today = date_today, age=age, height=height, weight=weight, image_path = image_path, badge_images = badge_images)

@app.route("/novasessao" , methods=['GET', 'POST'])
def pagina_novasessao():
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    return render_template('NovaSessao.html')

@app.route("/meusplanos/plano<selectedPlan>" , methods=['GET', 'POST'])
def pagina_mostrarplano(selectedPlan):
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    json_data = planosOrder()
    response, status_code = json_data
    if status_code == 200:
        json_data = response.json
        print(json_data)
    else:
        print(f"Error: Status Code {status_code}")
    
    id_real = json_data[selectedPlan]

    username = get_username(session['UserID'])
    
    return render_template('PlanoTreino.html', id_real = id_real, username = username)

#fim paginas base



#funções para a API	
@app.route("/planos" , methods=['GET', 'POST'])
def show_all_trainingPlans_from_user():                       #devolve todos os planos de treino do user
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
        if count > 6: #max 6 planos p/user
            break
        id = id[0]
        order[id] = count                                   #{id: order}
        training_plan = mgtreinos.getTrainingPlanData(id)
        training_plans_data[id] = training_plan             #{id: [name, description, type, duration, image]}
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




@app.route("/planotreino/<trainingPlanID>", methods=['GET', 'POST'])     #devolve info do plano de treino consoante o id
def show_trainingPlan(trainingPlanID):
   
    if 'UserID' not in session:
        return redirect(url_for('login'))
    
    training_plan_data = mgtreinos.getTrainingPlanData(trainingPlanID)
    if training_plan_data is None:
        return jsonify({'Error': 'Training plan not found'}), 404
    
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT ExercisePlanID FROM TrainingPlan WHERE TrainingPlanID = ?", (trainingPlanID,))
    exercisePlanId = cursor.fetchone()
    cursor.close()
    db.close()

    exercise_data = mgtreinos.get_exercise_data(exercisePlanId[0])
    
    return jsonify([training_plan_data, exercise_data]), 200  







if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
    
    