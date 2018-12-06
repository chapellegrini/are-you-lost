#!/usr/bin/env python3

from flask import Flask
from user import User
from database import Database

import json

app = Flask(__name__)

db = Database()

@app.route('/')
def index():
    return 'Hello!'

def getUserInfo(userid):
    return {
        'position': {
            'lattitude': db.users[userid].lattitude,
            'longitude': db.users[userid].longitude
        },
        'inventory': db.users[userid].inventory
    }

@app.route('/user/<user>')
def userInfo(user):
    userid = int(user)
    if userid < len(db.users):
        userDict = getUserInfo(userid)
        return json.dumps(userDict, indent=2)
    else:
        return 'Error: User does not exist'

@app.route('/users/')
def listUsers():
    usersDict = dict()
    for user in db.users.keys():
        usersDict[user] = getUserInfo(user)
    return json.dumps(usersDict, indent=2)

@app.route('/register/<name>')
def register(name):
    return str(db.addUser(name))
