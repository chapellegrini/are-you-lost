import math
class User:
    """The user class, carry bandages"""
    # Initializer / Instance attributes
    def __init__(self, uid, name, lattitude, longitude):
        self.uid = uid
        self.name = name
        self.lattitude = lattitude
        self.longitude = longitude
        self.inventory = {}

    def setCoordinate(self, lat, longi):
        self.lattitude = lat
        self.longitude = longi

    def publishItem(self, item, quantity=1):
        self.inventory[item] = quantity

    def have(self, item):
        if item in self.inventory:
            return true
        return false

    def removeItem(self,item):
        if item in self.inventory.keys():
            self.inventory[item]
            return True
        return False

    def getDistance(self,user):
        return math.sqrt((self.lattitude-user.lattitude)* (self.lattitude-user.lattitude) +  (self.longitude-user.longitude)* (self.longitude-user.longitude))

    def toJSON(self):
        return {
            'name': self.name,
            'position': {
                'lattitude': self.lattitude,
                'longitude': self.longitude
            },
            'inventory': self.inventory
        }

    def setLocalisation(self, lat, longi):
        self.lattitude=lat
        self.longitude=longi


if __name__ == "__main__":
    user=User(3,'tamere',10,10);
    user2=User(4,'tamere',10,20);
    print(user.getDistance(user2))
