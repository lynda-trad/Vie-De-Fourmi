import Ant


class Anthill:
    def __init__(self):
        self.__antNumber = 0   # Number of ants
        self.__roomArray = []  # [Sd, Sv, S1 ...] filled with Room objects
        self.__tunnel = []     # [(S1, Sd) , (S2, S3), ...]
        self.__antArray = []   # [ F1, F2, ...] filled with Ant objects

    def getRoomArray(self):
        return self.__roomArray

    def getAntArray(self):
        return self.__antArray

    def getLength(self):
        return len(self.__roomArray)

    def getAntNumber(self):
        return self.__antNumber

    def getTunnel(self):
        return self.__tunnel

    # Returns array filled with room names
    def getRoomNames(self):
        roomNames = []
        for room in self.__roomArray:
            roomNames.append(room.getName())
        return roomNames

    def setArray(self, a):
        self.__roomArray = a

    def setAntNumber(self, number):
        self.__antNumber = number

    # Adds room object to room array
    def addRoom(self, room):
        self.__roomArray.append(room)

    # Adds ant object to ants list
    def addAnts(self):
        for i in range(self.__antNumber):
            name = "F" + str(i + 1)
            self.__antArray.append(Ant.Ant(name, "1"))

    # Adds tuple of first and second room names to tunnel list
    def addTunnel(self, firstRoom, secondRoom):
        self.__tunnel.append((firstRoom, secondRoom))

    # Returns room object from room array when given its index
    def returnRoomWithIndex(self, index):
        for room in self.__roomArray:
            if room.getIndex() == index:
                return room

    # Returns room object from room array when given its name
    def returnRoomWithName(self, name):
        for room in self.__roomArray:
            if room.getName() == name:
                return room

    # Printing methods
    def printRooms(self):
        print("Anthill Room Array:")
        for r in self.__roomArray:
            print("---")
            r.printRoom()

    def printTunnels(self):
        print("Tunnels:", self.__tunnel)

    def printAntArray(self):
        print("Ant list:")
        for i in range(len(self.__antArray)):
            print("---")
            self.__antArray[i].printAnt()

    def printAnthill(self):
        print("\nAnt number :", self.__antNumber)
        print()
        self.printRooms()
        print()
        self.printTunnels()
        print()
        self.printAntArray()
        print()
