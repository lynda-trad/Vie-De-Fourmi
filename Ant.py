class Ant:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def setLocation(self, index):
        self.__location = index

    def printAnt(self):
        print("Ant :", self.getName())
        print("Location :", self.getLocation())
