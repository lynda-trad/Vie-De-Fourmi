class Room:
    def __init__(self, name, capacity, index):
        self.name = name
        self.maxCapacity = capacity
        self.index = index
        self.capacityLeft = capacity

    # Returns how many ants are allowed inside the room in total
    def getMaxCapacity(self):
        return self.maxCapacity

    # Returns how much room is left for a new ant to come inside
    def getCapacityLeft(self):
        return self.capacityLeft

    def getName(self):
        return self.name

    def getIndex(self):
        return self.index

    def setMaxCapacity(self, c):
        self.maxCapacity = c

    # When an ant comes in = True, capacityLeft decreases, if False, capacityLeft increases
    def setCapacityLeft(self, ant):
        if ant:
            if self.capacityLeft != 0:
                self.capacityLeft -= 1
            else:
                print("Error, the room can not fit anymore ants")
        else:
            if self.maxCapacity >= self.capacityLeft + 1:
                self.capacityLeft += 1
            else:
                print("Error, the room can not fit more ants than maxCapacity")

    # Returns True if an ant can enter the room, False if not
    def canEnter(self):
        if self.capacityLeft == 0:
            return False
        else:
            return True

    def printRoom(self):
        print("Name:", self.getName(), "Capacity:", self.getMaxCapacity(), "Index:", self.getIndex())
