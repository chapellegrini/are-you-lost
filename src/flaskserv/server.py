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

@app.route('/update', methods = ['PUT'] )
def updateLocalisation():
    latitude = float(request.form['lat'])
    longitude = float(request.form['long'])
    user = db.users[session['id']]
    user.setLocation(latitude, longitude)


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
    latitude = float(request.args['lat'])
    longitude = float(request.args['long'])
    session['id']= db.addUser(name, latitude, longitude)
    return 'OK'

@app.route('/item')
def getUsersWithItem():
    dist=getRequestArg('dist',150)
    quantity=getRequestArg('quantity',1)
    item==request.args['item']
    users= db.getUsersByItem(item, quantity, dist)
    listJson=[]
    for user in users:
        listJson.append(user.toJSON())
    return listJson

def getRequestArg(string, default):
    if string in request.args.keys():
        return request.args[string]
    return default

@app.route('/additem/', methods = ['POST'])
def addItem():
    item = request.form['item']
    nbitems = int(request.form['nb'])
    user = db.users[session['id']]
    user.publishItem(item, quantity=nbitems)
    return 'OK'

@app.route('/delitem/', methods = ['DELETE'])
def delItem():
    item = request.form['item']
    user = db.users[session['id']]
    user.removeItem(item)

