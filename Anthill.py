import Room
import Ant
import numpy


class Anthill:
    def __init__(self):
        self.antNumber = 0   # Number of ants
        self.roomArray = []  # [Sd, Sv, S1 ...] filled with Room objects
        self.tunnel = []     # [(S1, Sd) , (S2, S3), ...]
        self.antArray = []   # [ F1, F2, ...] filled with Ant objects

    # Returns array filled with room names
    def getRoomNames(self):
        roomNames = []
        for room in self.getRoomArray():
            roomNames.append(room.getName())
        return roomNames

    def getRoomArray(self):
        return self.roomArray

    def getAntArray(self):
        return self.antArray

    def getLength(self):
        return len(self.roomArray)

    def getAntNumber(self):
        return self.antNumber

    def getTunnel(self):
        return self.tunnel

    def setArray(self, a):
        self.roomArray = a

    def setAntNumber(self, number):
        self.antNumber = number

    # Adds room object to room array
    def addRoom(self, room):
        self.roomArray.append(room)

    # Adds ant object to ants list
    def addAnts(self):
        for i in range(self.antNumber):
            name = "F" + str(i + 1)
            self.antArray.append(Ant.Ant(name, "1"))

    # Adds tuple of first and second room names to tunnel list
    def addTunnel(self, firstRoom, secondRoom):
        self.tunnel.append((firstRoom, secondRoom))

    # Returns room object from room array when given its index
    def returnRoomWithIndex(self, index):
        for room in self.roomArray:
            if room.getIndex() == index:
                return room

    # Returns room object from room array when given its name
    def returnRoomWithName(self, name):
        for room in self.roomArray:
            if room.getName() == name:
                return room

    # Printing methods
    def printRooms(self):
        print("Anthill Room Array:")
        for r in self.roomArray:
            print("---")
            r.printRoom()

    def printTunnels(self):
        print("Tunnels:", self.tunnel)

    def printAntArray(self):
        print("Ant list:")
        for i in range(len(self.antArray)):
            print("---")
            self.antArray[i].printAnt()

    def printAnthill(self):
        print("\nAnt number :", self.getAntNumber())
        print()
        self.printRooms()
        print()
        self.printTunnels()
        print()
        self.printAntArray()
        print()
