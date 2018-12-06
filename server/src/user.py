class User:
    """The user class, carry bandages"""
    # Initializer / Instance attributes
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.lattitude = None
        self.longitude = None
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
