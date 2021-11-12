import Ant


class Anthill:
    def __init__(self):
        self._antNumber = 0   # Number of ants
        self._roomArray = []  # [Sd, Sv, S1 ...] filled with Room objects
        self._tunnel = []     # [(S1, Sd) , (S2, S3), ...]
        self._antArray = []   # [ F1, F2, ...] filled with Ant objects

    def getRoomArray(self):
        return self._roomArray

    def getAntArray(self):
        return self._antArray

    def getLength(self):
        return len(self._roomArray)

    def getAntNumber(self):
        return self._antNumber

    def getTunnel(self):
        return self._tunnel

    # Returns array filled with room names
    def getRoomNames(self):
        roomNames = []
        for room in self._roomArray:
            roomNames.append(room.getName())
        return roomNames

    def setArray(self, a):
        self._roomArray = a

    def setAntNumber(self, number):
        self._antNumber = number

    # Adds room object to room array
    def addRoom(self, room):
        self._roomArray.append(room)

    # Adds ant object to ants list
    def addAnts(self):
        for i in range(self._antNumber):
            name = "F" + str(i + 1)
            self._antArray.append(Ant.Ant(name, "1"))

    # Adds tuple of first and second room names to tunnel list
    def addTunnel(self, firstRoom, secondRoom):
        self._tunnel.append((firstRoom, secondRoom))

    # Returns room object from room array when given its index
    def returnRoomWithIndex(self, index):
        for room in self._roomArray:
            if room.getIndex() == index:
                return room

    # Returns room object from room array when given its name
    def returnRoomWithName(self, name):
        for room in self._roomArray:
            if room.getName() == name:
                return room

    # Printing methods
    def printRooms(self):
        print("Anthill Room Array:")
        for r in self._roomArray:
            print("---")
            r.printRoom()

    def printTunnels(self):
        print("Tunnels:", self._tunnel)

    def printAntArray(self):
        print("Ant list:")
        for i in range(len(self._antArray)):
            print("---")
            self._antArray[i].printAnt()

    def printAnthill(self):
        print("\nAnt number :", self.getAntNumber())
        print()
        self.printRooms()
        print()
        self.printTunnels()
        print()
        self.printAntArray()
        print()
