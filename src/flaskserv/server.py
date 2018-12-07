#!/usr/bin/env python3

from flask import Flask, request
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
    currentUser= db.getUser(session['id'])
    getRequestArg('dist',150)
    usersDict = dict()
    for user in db.users.keys():
        if currentUser.getDistance(user)<maxDist:
            usersDict[user] = getUserInfo(user)
    return json.dumps(usersDict, indent=2)

@app.route('/register/')
def register():
    name= request.args['name']

    lattitude = request.args['lattitude']
    longitude = request.args['longitude']
    session['id']= db.addUser(name, lattitude, longitude)
    return 'OK' 

def getRequestArg(string, default):
    if string in request.args.keys():
        return request.args[string]
    return default
