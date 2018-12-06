#!/usr/bin/env python3

from flask import Flask
from user import User
from database import Database
from flask import request

import json

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    return 'Hello!'

def getUserInfo(userid):
    return {
        'name': db.users[userid].name,
        'position': {
            'lattitude': db.users[userid].lattitude,
            'longitude': db.users[userid].longitude
        },
        'inventory': db.users[userid].inventory
    }

@app.route('/user/<userid>')
def userInfo(userid):
    if userid in db.users.keys():
        userDict = getUserInfo(userid)
        return json.dumps(userDict, indent=2)
    else:
        return 'Error: User does not exist'

@app.route('/users/')
def listUsers():
    usersList = list()
    i = 0
    for userid in db.users.keys():
        usersList.append(getUserInfo(userid))
    return json.dumps(usersList, indent=2)

@app.route('/register/<name>')
def register(name):
    session['id']= db.addUser(name)
    return 'OK'
