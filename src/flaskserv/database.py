from user import User
class Database:
    """The user class, carry bandages"""
    # Initializer / Instance attributes

    def __init__(self):
        self.users = {}

    def getUser(self, uid):
        return self.users[uid]

    def addUser(self, name):
        randint=random.randint(0,1000000);
        while randint in users.keys:
            randint=random.randint(0,1000000);
        user = User(randint,name)
        self.users[randint]=user;
        return randint

    def getUsersByItem(self, item):
        res = []
        for user in self.users:
            if user.have(item):
                res.append(user)
        return res


