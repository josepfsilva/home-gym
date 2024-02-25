from flask import Flask
from flask import render_template
import sqlite3
from datetime import date, timedelta, datetime


def getbadges_type(userID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT BadgeID
                   FROM UserBadges
                   WHERE UserID = ?
                   """, (userID,))
    badges_id = cursor.fetchall()
    db.close()

    return badges_id

def getbadges_data(badgeID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT Name, Description, Type, Image
                   FROM BadgeType
                   WHERE BadgeID = ?
                   """, (badgeID,))
    badge_data = cursor.fetchone()
    db.close()
    
    return badge_data


#check badges
def badges(userID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT BadgeID
                   FROM UserBadges
                   WHERE UserID = ?
                   """, (userID,))
    badges_id = [item for sublist in cursor.fetchall() for item in sublist]
    print(badges_id) #mostra badges ja atribuidas
    db.close()

    badge_checks = {1: badge_check_1, 2: badge_check_2}  

    for badge_id, check_func in badge_checks.items():
        if badge_id not in badges_id:
            check_func(userID)
    return


def badge_check_1(userID): #badge 1
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT FinishTrainingID
                   FROM FinishTraining
                   WHERE UserID = ?
                   """, (userID,))
    fin = cursor.fetchone()
    db.close()

    if fin: #se existir um registo de treino
        Awdate = date.today()
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("""INSERT INTO UserBadges (DateAwarded, UserID, BadgeID)
                       VALUES (?, ?, 1)
                       """, (Awdate,userID,))
        db.commit()
        db.close()
    return


def badge_check_2(userID): #badge 2
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT FinishDate, COUNT(*)
                      FROM FinishTraining
                      WHERE UserID = ?
                      GROUP BY FinishDate
                      HAVING COUNT(*) >= 3
                   """, (userID,))
    result = cursor.fetchone()
    db.close()

    if result:  # If there is a day with at least 3 records
        date = result[0]  # The date of the day with at least 3 records
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("""INSERT INTO UserBadges (DateAwarded, UserID, BadgeID)
                          VALUES (?, ?, 2)
                       """, (date, userID,))
        db.commit()
        db.close()
    return


    

