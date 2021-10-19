import Room
import Ant
import numpy


class Anthill:
    def __init__(self):
        self.antNumber = 0  # Number of ants
        self.roomArray = []     # [Sd, Sv, S1 ...] filled with Room objects
        self.tunnel = []    # [(S1, Sd) , (S2, S3), ...]
        self.antArray = []  # [ F1, F2, ...] filled with Ant objects

    # Returns array filled with room names
    def getNames(self):
        roomNames = []
        for room in self.getRoomArray():
            roomNames.append(room.getName())
        return roomNames

    def getRoomArray(self):
        return self.roomArray

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

    def addRoom(self, room):
        self.roomArray.append(room)

    def addAnts(self):
        for i in range(self.antNumber):
            name = "F" + str(i + 1)
            self.antArray.append(Ant.Ant(name, "Sv"))

    def addTunnel(self, firstRoom, secondRoom):
        self.tunnel.append((firstRoom, secondRoom))

    # Returns room object from room array when given its name
    def returnRoom(self, name):
        for room in self.roomArray:
            if room.getName() == name:
                return room

    # Printing methods
    def printRooms(self):
        print("Anthill Room Array:")
        for r in self.roomArray:
            r.printRoom()

    def printTunnels(self):
        print("Tunnels:", self.tunnel)

    def printAnthill(self):
        print("Ant number :", self.getAntNumber())
        self.printRooms()
        self.printTunnels()
        print("Ant list:")
        for i in range(len(self.antArray)):
            self.antArray[i].printAnt()
