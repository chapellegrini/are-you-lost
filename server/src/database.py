from user import User
class Database:
    """The user class, carry bandages"""
    # Initializer / Instance attributes
    cpt=0
    def __init__(self):
        self.users = []

    def getUser(self, userNum):
        return users[usersNum]

    def addUser(self, name):
        user= User(cpt,name)
        cpt=cpt+1
        users.append(user)
        return cpt

    def getUsersByItem(self, item):
        res=[]
        for user in users:
            if user.have(item):
                res.append(user)
        return res
