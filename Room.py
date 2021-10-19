class Room:
    def __init__(self, name, capacity, index):
        self.name = name
        self.capacity = capacity
        self.index = index

    def getCapacity(self):
        return self.capacity

    def getName(self):
        return self.name

    def getIndex(self):
        return self.index

    def setCapacity(self, c):
        self.capacity = c

    def printRoom(self):
        print("Name:", self.getName(), "Capacity:", self.getCapacity(), "Index:", self.getIndex())
