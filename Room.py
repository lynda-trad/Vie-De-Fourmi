# Room of the anthill

# Init of Sd and Sv


class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def setCapacity(self, c):
        self.capacity = c

    def getCapacity(self):
        return self.capacity

    def getName(self):
        return self.name

    def printRoom(self):
        print("Name:", self.getName(), "Capacity:", self.getCapacity())
