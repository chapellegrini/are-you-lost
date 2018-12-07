#!/usr/bin/env python3

from flask import Flask, request, session
from user import User
from database import Database

import json

app = Flask(__name__)
app.secret_key = 'any random string'
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
    currentUser= db.getUser(session['id'])
    maxDist = getRequestArg('dist',150)
    usersList = list()
    for user in db.users.keys():
        if currentUser.getDistance(db.getUser(user))<maxDist:
            usersList.append(getUserInfo(user))
    return json.dumps(usersList, indent=2)

@app.route('/register/')
def register():
    name= getRequestArg('name','anonymous')
    lattitude = float(request.args['lattitude'])
    longitude = float(request.args['longitude'])
    session['id']= db.addUser(name, lattitude, longitude)
    return 'OK' 

def getRequestArg(string, default):
    if string in request.args.keys():
        return request.args[string]
    return default

