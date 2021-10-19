import Room
import Ant
import numpy


class Anthill:
    def __init__(self):
        self.antNumber = 0  # Number of ants
        self.array = []     # [Sd, Sv, S1 ...] filled with Room objects
        self.tunnel = []    # [(S1, Sd) , (S2, S3), ...]
        self.antArray = []  # [ F1, F2, ...] filled with Ant objects

    def getArray(self):
        return self.array

    def getLength(self):
        return len(self.array)

    def setArray(self, a):
        self.array = a

    def setAntNumber(self, number):
        self.antNumber = number

    def getAntNumber(self):
        return self.antNumber

    def getTunnel(self):
        return self.tunnel

    def getNames(self):
        roomNames = []
        for room in self.getArray():
            roomNames.append(room.getName())
        return roomNames

    def addRoom(self, room):
        self.array.append(room)

    def addAnts(self):
        for i in range(self.antNumber):
            name = "F" + str(i + 1)
            self.antArray.append(Ant.Ant(name, "Sv"))

    def printRooms(self):
        print("Anthill Room Array:")
        for r in self.array:
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

    def addTunnel(self, firstRoom, secondRoom):
        self.tunnel.append((firstRoom, secondRoom))

    def returnRoom(self, name):
        for room in self.array:
            if room.getName() == name:
                return room
