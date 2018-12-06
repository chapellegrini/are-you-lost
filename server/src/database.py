from user import User
class Database:
    """The user class, carry bandages"""
    # Initializer / Instance attributes

    cpt = 0
    def __init__(self):
        self.users = []

    def getUser(self, userNum):
        return self.users[usersNum]

    def addUser(self, name):
        user = User(Database.cpt,name)
        Database.cpt += 1
        self.users.append(user)
        return Database.cpt - 1

    def getUsersByItem(self, item):
        res = []
        for user in self.users:
            if user.have(item):
                res.append(user)
        return res
