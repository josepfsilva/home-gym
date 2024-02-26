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
    badge_awarded = []

    for badge_id, check_func in badge_checks.items():
        if badge_id not in badges_id:
            if check_func(userID):
                badge_awarded.append(badge_id)

    return badge_awarded


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
        return True  # Badge awarded
    
    return False


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
        return True # Badge awarded
    
    return False 

def streak(userID):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("""SELECT FinishDate
                   FROM FinishTraining
                   WHERE UserID = ?
                   ORDER BY FinishDate
                   """, (userID,))
    data = cursor.fetchall()
    db.close()

    if not data:  # If there are no records
        return 0
    
    dates = sorted(set([datetime.strptime(date[0], "%Y-%m-%d").date() for date in data]), reverse=True)
    print(dates)
    streak = 0
    current_date = datetime.now().date()

    for date in dates:
        # If the date is today or yesterday, increment the streak and continue to the previous day
        if date == current_date or date == current_date - timedelta(days=1):
            streak += 1
            current_date -= timedelta(days=1)
        # If the date is not consecutive, break the loop
        else:
            break

    return streak

