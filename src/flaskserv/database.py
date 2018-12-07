from user import User
import random

class Database:
    """The user class, carry bandages"""
    # Initializer / Instance attributes

    def __init__(self):
        self.users = {}

    def getUser(self, uid):
        return self.users[uid]


    def addUser(self, name,lattitude,longitude):
        rnd = random.randint(0,1000000);
        while rnd in self.users.keys():
            rnd = randint(0,1000000);
        user = User(rnd, name,lattitude,longitude)
        self.users[rnd] = user;
        return rnd

    def getUsersByItem(self, item, minimalQuantity=1, maxDistance=150):
        res = []
        for user in self.users:
            if user.have(item):
                res.append(user)
        return res


