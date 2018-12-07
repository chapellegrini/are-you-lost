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

@app.route('/user/<userid>')
def userInfo(userid):
    if userid in db.users.keys():
        userDict = db.users[userid].toJSON()
        return json.dumps(userDict, indent=2)
    else:
        return 'Error: User does not exist'

@app.route('/users/')
def listUsers():
    currentUser= db.getUser(session['id'])
    maxDist = getRequestArg('dist',150)
    usersList = list()
    for userid in db.users:
        user = db.getUser(userid)
        if currentUser.getDistance(user)<maxDist:
            usersList.append(user.toJSON())
    return json.dumps(usersList, indent=2)

@app.route('/register/')
def register():
    name= getRequestArg('name','anonymous')
    lattitude = float(request.args['lattitude'])
    longitude = float(request.args['longitude'])
    session['id']= db.addUser(name, lattitude, longitude)
    return 'OK'
"""
@app.route('/item')
def getUsersWithItem():
    item==request.args['item']
    users= db.getUsersByItem(item)
    for user in users:
"""

def getRequestArg(string, default):
    if string in request.args.keys():
        return request.args[string]
    return default

@app.route('/additem/', methods = ['POST'])
def additem():
    item = request.form['item']
    nbitems = int(request.form['nb'])
    user = db.users[session['id']]
    user.publishItem(item, quantity=nbitems)
    return 'OK'
