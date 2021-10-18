import Room


class Anthill:
    def __init__(self):
        self.array = []
        self.length = len(self.array)
        self.antNumber = 0

    def getArray(self):
        return self.array

    def getLength(self):
        return self.length

    def setArray(self, a):
        self.array = a

    def setAntNumber(self, number):
        self.antNumber = number

    def addRoom(self, room):
        self.array.append(room)
