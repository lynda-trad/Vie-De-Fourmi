class Ant:
    def __init__(self, name, location):
        self._name = name
        self._location = location

    def getName(self):
        return self._name

    def getLocation(self):
        return self._location

    def setLocation(self, index):
        self._location = index

    def printAnt(self):
        print("Ant :", self.getName())
        print("Location :", self.getLocation())
