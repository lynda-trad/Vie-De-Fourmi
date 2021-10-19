class Ant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def setLocation(self, room):
        self.location = room

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def printAnt(self):
        print("Ant :", self.getName())
        print("Location :", self.getLocation())
