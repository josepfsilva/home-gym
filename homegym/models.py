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
    tables = ['sqlite_sequence','BadgeType', 'ExercisePlan', 'Exercises', 'FinishTraining', 'Food', 'Friendship', 'Measurements', 'Nutrition', 'TrainingPlan', 'UserBadges', 'Users']

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
        INSERT OR IGNORE INTO Users (Username, Password, Name, Surname, Email, BirthDate, RegistrationDate, Role, Status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ('Maria', '1234', 'Maria','Santos','testuser@example.com', '1960-01-01', date.today(), 'User', 'Online'))
    c.execute("""
        INSERT OR IGNORE INTO Users (Username, Password, Name, Surname, Email, BirthDate, RegistrationDate, Role, Status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ('Jorge', '1234', 'Jorge', 'Fernandes', 'testuser2@example.com', '1955-12-05', date.today(), 'User', 'Online'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def add_exercises():
    # Connect to the SQLite database
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    #upper body
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Flexões', 'Um exercício de corpo inteiro que trabalha o peito, ombros e tríceps.', 'https://www.youtube.com/watch?v=WDIpL0pjun0','static\\img\\flexao.jpg' ,'Musculacao', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg, Type, Difficulty) VALUES ('Flexões em diamante', 'Um exercício de corpo inteiro que trabalha o peito, ombros e tríceps.', 'https://www.youtube.com/watch?v=XtU2VQVuLYs', 'static\\img\\flexao.jpg' ,'Musculacao', 'Hard');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg, Type, Difficulty) VALUES ('Abdominais', 'Um exercício de corpo inteiro que trabalha o core.', 'http://example.com/crunches','static\\img\\flexao.jpg' , 'Musculacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Flexões de Parede', 'Trabalha os músculos do peito, ombros e braços.', 'http://example.com/wall-push-ups', 'static\\img\\flexao.jpg' ,'Musculacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Elevação de Halteres Sentado', 'Trabalha os músculos dos ombros.', 'http://example.com/seated-dumbbell-shoulder-press', 'static\\img\\flexao.jpg' ,'Musculacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Puxada com Faixa Elástica', 'Fortalece os músculos das costas.', 'http://example.com/resistance-band-pull', 'static\\img\\flexao.jpg' ,'Musculacao', 'Easy');")

    #lower body
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Agachamentos', 'Um exercício composto que trabalha os quadríceps, isquiotibiais e glúteos.', 'http://example.com/squats', 'static\\img\\flexao.jpg' ,'Musculacao', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Lunges', 'Um exercício de perna que trabalha os quadríceps e glúteos.', 'http://example.com/lunges', 'static\\img\\flexao.jpg' ,'Musculacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Agachamentos com salto', 'Um exercício de perna que trabalha os quadríceps e glúteos.', 'http://example.com/jump-squats', 'static\\img\\flexao.jpg' ,'Musculacao', 'Hard');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Agachamento com Faixa Elástica', 'Trabalha os músculos das pernas e glúteos.', 'http://example.com/resistance-band-squats', 'static\\img\\flexao.jpg' ,'Musculacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Elevação de Pernas Sentado', 'Trabalha os músculos das pernas.', 'http://example.com/seated-leg-raise', 'static\\img\\flexao.jpg' ,'Musculacao', 'Easy');")
    
    #cardio
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Polichinelos', 'Um exercício de cardio de corpo inteiro que pode ser feito em casa.', 'http://example.com/jumping-jacks', 'static\\img\\flexao.jpg' ,'Cardio', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Burpees', 'Um exercício de cardio de corpo inteiro que combina agachamentos, saltos e flexões.', 'http://example.com/burpees', 'static\\img\\flexao.jpg' ,'Cardio', 'Hard');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Mountain Climbers', 'Um exercício de cardio que também trabalha o core.', 'http://example.com/mountain-climbers', 'static\\img\\flexao.jpg' ,'Cardio', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Corrida no Local', 'Um exercício que aumenta a frequência cardíaca e queima calorias, simulando o movimento de correr, mas sem sair do lugar.', 'http://example.com/jogging-in-place', 'static\\img\\flexao.jpg' ,'Cardio', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Saltar à Corda', 'Trabalha a coordenação, resistência e queima calorias.', 'http://example.com/jump-rope','static\\img\\flexao.jpg' , 'Cardio', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg,Type, Difficulty) VALUES ('Step Aeróbico', 'Aumenta a frequência cardíaca e trabalha os músculos das pernas.', 'http://example.com/step-aerobics','static\\img\\flexao.jpg' , 'Cardio', 'Medium');")

    #meditacao
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Meditação', 'Um exercício de relaxamento que ajuda a aliviar o stress.', 'http://example.com/meditation', 'static\\img\\flexao.jpg' ,'Meditacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Meditação2', 'Um exercício de relaxamento que ajuda a aliviar o stress.', 'http://example.com/meditation', 'static\\img\\flexao.jpg' ,'Meditacao', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Meditação3', 'Um exercício de relaxamento que ajuda a aliviar o stress.', 'http://example.com/meditation', 'static\\img\\flexao.jpg' ,'Meditacao', 'Easy');")

    #alongamentos membros superiores
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Ombros', 'Este alongamento ajuda a alongar os músculos dos ombros e do pescoço.', 'http://exemplo.com/alongamento-ombros', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Bíceps', 'Este alongamento foca nos músculos do bíceps.', 'http://exemplo.com/alongamento-biceps', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Tríceps', 'Este exercício alonga os músculos do tríceps na parte de trás dos braços.', 'http://exemplo.com/alongamento-triceps', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento dos Flexores do Pulso', 'Ajuda a alongar os músculos do antebraço e dos pulsos.', 'http://example.com/wrist-flexor-stretch', 'static\\img\\flexao.jpg' ,'Alongamento', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Costas', 'Este alongamento alonga os músculos das costas.', 'http://exemplo.com/alongamento-costas', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")

    #alongamentos membros inferiores
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Quadríceps', 'Este alongamento foca nos músculos dos quadríceps na parte da frente das coxas.', 'http://exemplo.com/alongamento-quadriceps', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Isquiotibiais', 'Este alongamento ajuda a alongar os músculos dos isquiotibiais na parte de trás das coxas.', 'http://exemplo.com/alongamento-isquiotibiais', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Panturrilhas', 'Este alongamento alonga os músculos das panturrilhas na parte de trás das pernas.', 'http://exemplo.com/alongamento-panturrilhas', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento dos Flexores do Quadril', 'Ajuda a alongar os músculos da parte frontal da coxa e do quadril.', 'http://example.com/hip-flexor-stretch', 'static\\img\\flexao.jpg' ,'Alongamento', 'Medium');")
    cursor.execute("INSERT OR IGNORE INTO Exercises (Name, Description, URL, ExerciseImg ,Type, Difficulty) VALUES ('Alongamento de Glúteos', 'Este alongamento foca nos músculos dos glúteos.', 'http://exemplo.com/alongamento-gluteos', 'static\\img\\flexao.jpg' ,'Alongamento', 'Easy');")
   
    #ver as dificuldades

    db.commit()
    db.close()


def add_exercise_plan():    
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    #upper body
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (1, 2, 3);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (4, 5, 6);")
    
    #lower body
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (7, 8, 9);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (9, 10, 11);")
    
    #cardio
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (12, 13, 14);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (15, 16, 17);")

    #meditacao
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (18, 19, 20);")

    #alongamentos membros superiores
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (21, 22, 23);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (23, 24, 25);")

    #alongamentos membros inferiores
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (26, 27, 28);")
    cursor.execute("INSERT OR IGNORE INTO ExercisePlan (Exercise1, Exercise2, Exercise3) VALUES (28, 29, 30);")
    db.commit()
    db.close()

def add_training_plan():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    
    #user1
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Treino de parte superior', 'Este plano visa a trabalhar a parte superior do corpo.', 'Musculacao', 'Easy', 90, 'static\\img\\upper-body.jpg' ,1, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Treino de parte inferior', 'Este plano visa a trabalhar a parte inferior do corpo.', 'Musculacao','Easy', 90,'static\\img\\lower-body.jpg', 3, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Treino de cardio', 'O objetivo deste plano é aumentar a resistencia.', 'Cardio','Easy', 90, 'static\\img\\cardio.jpg',5, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Meditacao', 'Este plano tem como objetivo promover o relaxamento e a saúde mental.', 'Meditacao','Easy', 90, 'static\\img\\meditation.jpg',7, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Alongamentos membros superiores', 'A finalidade deste plano é melhorar a flexibilidade e aliviar a tensão muscular dos membros superiores.', 'Musculacao', 'Easy',90, 'static\\img\\upper-stretches.jpg',8, 1);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Alongamentos membros inferiores', 'A finalidade deste plano é melhorar a flexibilidade e aliviar a tensão muscular dos membros inferiores', 'Musculacao', 'Easy',90, 'static\\img\\lower-stretches.jpg',10, 1);")

    #user2
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Treino de parte superior', 'Este plano visa a trabalhar a parte superior do corpo.', 'Musculacao', 'Easy',90, 'static\\img\\upper-body.jpg',2, 2);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Treino de parte inferior', 'Este plano visa a trabalhar a parte inferior do corpo.', 'Musculacao', 'Easy',90, 'static\\img\\lower-body.jpg',4, 3);") #changed user to 3 to test
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Treino de cardio', 'O objetivo deste plano é aumentar a resistencia.', 'Cardio','Easy', 90, 'static\\img\\cardio.jpg',6, 2);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Meditacao', 'Este plano tem como objetivo promover o relaxamento e a saúde mental.', 'Meditacao','Easy', 90, 'static\\img\\meditation.jpg', 7, 2);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Alongamentos membros superiores', 'A finalidade deste plano é melhorar a flexibilidade e aliviar a tensão muscular dos membros superiores.', 'Musculacao','Easy', 90,'static\\img\\upper-stretches.jpg', 9, 2);")
    cursor.execute("INSERT OR IGNORE INTO TrainingPlan (Name, Description, Type, Difficulty, PlanDuration, TrainImage,ExercisePlanID, UserID) VALUES ('Alongamentos membros inferiores', 'A finalidade deste plano é melhorar a flexibilidade e aliviar a tensão muscular dos membros inferiores', 'Musculacao', 'Easy',90,'static\\img\\lower-stretches.jpg', 11, 2);")

    db.commit()
    db.close()

def get_username(userID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT Username FROM Users WHERE UserID = ?", (userID,))
    username = cursor.fetchone()
    db.close()
    return username[0]

def get_user_data(userID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Users WHERE UserID = ?", (userID,))
    user_data = cursor.fetchone()
    db.close()
    return list(user_data)

def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
    
