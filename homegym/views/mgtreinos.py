from flask import Flask
from flask import render_template
import sqlite3

def getUserTrainingPlans(userID):

    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT TrainingPlanID
                   FROM TrainingPlan
                   WHERE UserID = ?
                   """, (userID,))
    training_plans = cursor.fetchall()
    db.close()

    return training_plans

def getTrainingPlanData(trainingPlanID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT Name, Description, Type
                   FROM TrainingPlan
                   WHERE TrainingPlanID = ?
                   """, (trainingPlanID,))
    training_plan_data = cursor.fetchone()
    db.close()
    return training_plan_data


def get_exercise_data(exercisePlanID):
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
                WHERE ExercisePlan.ExercisePlanID = ?
                        """, (exercisePlanID,))
        
    exercise_data = cursor.fetchone()
    db.close()
        
    exercises = [exercise_data[i:i+4] for i in range(0,len(exercise_data),4)]