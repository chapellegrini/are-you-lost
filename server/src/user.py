class User:
    """The user class, carry bandages"""
    # Initializer / Instance attributes
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.lattitude=None
        self.longitude=None
        self.inventory = []


    def setCoordinate(self, lat, longi):
        lattitude=lat
        longitude=longi


    def addItem(self, item):
        inventory.append(item)
