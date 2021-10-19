class Ant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def setLocation(self, index):
        self.location = index

    def printAnt(self):
        print("Ant :", self.getName())
        print("Location :", self.getLocation())
