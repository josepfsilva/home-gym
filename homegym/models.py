import sqlite3


"""
def get_db_Users():
    db_users = sqlite3.connect('Users.db')
    db_users.row_factory = sqlite3.Row
    db_users.execute("PRAGMA foreign_keys = ON;")
    return db_users

def init_db_Users():
    from app import app
    with app.app_context():
        db_users = get_db_Users()
        with app.open_resource('databases/Users.sql', mode='r') as f:
            db_users.cursor().executescript(f.read())
        db_users.commit()
    
def get_db_BadgeType():
    db_badgetype = sqlite3.connect('BadgeType.db')
    db_badgetype.row_factory = sqlite3.Row
    db_badgetype.execute("PRAGMA foreign_keys = ON;")
    return db_badgetype

def init_db_BadgeType():
    from app import app
    with app.app_context():
        db_badgetype = get_db_BadgeType()
        with app.open_resource('databases/BadgeType.sql', mode='r') as f:
            db_badgetype.cursor().executescript(f.read())
        db_badgetype.commit()
        
def get_db_Exercises():
    db_exercises = sqlite3.connect('Exercises.db')
    db_exercises.row_factory = sqlite3.Row
    db_exercises.execute("PRAGMA foreign_keys = ON;")
    return db_exercises

def init_db_Exercises():
    from app import app
    with app.app_context():
        db_exercises = get_db_Exercises()
        with app.open_resource('databases/Exercises.sql', mode='r') as f:
            db_exercises.cursor().executescript(f.read())
        db_exercises.commit()
        
def get_db_FinishTraining():
    db_finishtraining = sqlite3.connect('FinishTraining.db')
    db_finishtraining.row_factory = sqlite3.Row
    db_finishtraining.execute("PRAGMA foreign_keys = ON;")
    return db_finishtraining

def init_db_FinishTraining():
    from app import app
    with app.app_context():
        db_finishtraining = get_db_FinishTraining()
        with app.open_resource('databases/FinishTraining.sql', mode='r') as f:
            db_finishtraining.cursor().executescript(f.read())
        db_finishtraining.commit()
        
def get_db_Food():
    db_food = sqlite3.connect('Food.db')
    db_food.row_factory = sqlite3.Row
    db_food.execute("PRAGMA foreign_keys = ON;")
    return db_food

def init_db_Food():
    from app import app
    with app.app_context():
        db_food = get_db_Food()
        with app.open_resource('databases/Food.sql', mode='r') as f:
            db_food.cursor().executescript(f.read())
        db_food.commit()
        
def get_db_Friendship():
    db_friendship = sqlite3.connect('Friendship.db')
    db_friendship.row_factory = sqlite3.Row
    db_friendship.execute("PRAGMA foreign_keys = ON;")
    return db_friendship

def init_db_Friendship():
    from app import app
    with app.app_context():
        db_friendship = get_db_Friendship()
        with app.open_resource('databases/Friendship.sql', mode='r') as f:
            db_friendship.cursor().executescript(f.read())
        db_friendship.commit()
        
def get_db_Measurements():
    db_measurements = sqlite3.connect('Measurements.db')
    db_measurements.row_factory = sqlite3.Row
    db_measurements.execute("PRAGMA foreign_keys = ON;")
    return db_measurements

def init_db_Measurements():
    from app import app
    with app.app_context():
        db_measurements = get_db_Measurements()
        with app.open_resource('databases/Measurements.sql', mode='r') as f:
            db_measurements.cursor().executescript(f.read())
        db_measurements.commit()
        
def get_db_Nutrition():
    db_nutrition = sqlite3.connect('Nutrition.db')
    db_nutrition.row_factory = sqlite3.Row
    db_nutrition.execute("PRAGMA foreign_keys = ON;")
    return db_nutrition

def init_db_Nutrition():
    from app import app
    with app.app_context():
        db_nutrition = get_db_Nutrition()
        with app.open_resource('databases/Nutrition.sql', mode='r') as f:
            db_nutrition.cursor().executescript(f.read())
        db_nutrition.commit()
        
def get_db_ExercisePlan():
    db_ExercisePlan = sqlite3.connect('ExercisePlan.db')
    db_ExercisePlan.row_factory = sqlite3.Row
    db_ExercisePlan.execute("PRAGMA foreign_keys = ON;")
    return db_ExercisePlan

def init_db_ExercisePlan():
    from app import app
    with app.app_context():
        db_ExercisePlan = get_db_ExercisePlan()
        with app.open_resource('databases/ExercisePlan.sql', mode='r') as f:
            db_ExercisePlan.cursor().executescript(f.read())
        db_ExercisePlan.commit()
        
def get_db_TrainingPlan():
    db_TrainingPlan = sqlite3.connect('TrainingPlan.db')
    db_TrainingPlan.row_factory = sqlite3.Row
    db_TrainingPlan.execute("PRAGMA foreign_keys = ON;")
    return db_TrainingPlan

def init_db_TrainingPlan():
    from app import app
    with app.app_context():
        db_TrainingPlan = get_db_TrainingPlan()
        with app.open_resource('databases/TrainingPlan.sql', mode='r') as f:
            db_TrainingPlan.cursor().executescript(f.read())
        db_TrainingPlan.commit()
        
def get_db_UserBadges():
    db_userbadges = sqlite3.connect('UserBadges.db')
    db_userbadges.row_factory = sqlite3.Row
    db_userbadges.execute("PRAGMA foreign_keys = ON;")
    return db_userbadges

def init_db_UserBadges():
    from app import app
    with app.app_context():
        db_userbadges = get_db_UserBadges()
        with app.open_resource('databases/UserBadges.sql', mode='r') as f:
            db_userbadges.cursor().executescript(f.read())
        db_userbadges.commit()

    
    """
    


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

