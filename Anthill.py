import Room
import numpy


class Anthill:
    def __init__(self):
        self.antNumber = 0  # Number of ants
        self.array = []  # [Sd, Sv, S1 ...] fill with Room objects
        self.tunnel = []  # [(S1, Sd) , (S2, S3), ...]

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

    def addTunnel(self, firstRoom, secondRoom):
        self.tunnel.append((firstRoom, secondRoom))

    def returnRoom(self, name):
        for room in self.array:
            if room.getName() == name:
                return room
