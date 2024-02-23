from flask import Flask
from flask import render_template
import sqlite3


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

