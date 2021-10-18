import Room


class Anthill:
    def __init__(self):
        self.array = []
        self.length = len(self.array)
        self.antNumber = 0
        self.matrice =[]

    def getArray(self):
        return self.array

    def getLength(self):
        return self.length

    def setArray(self, a):
        self.array = a

    def setAntNumber(self, number):
        self.antNumber = number

    def getAntNumber(self):
        return self.antNumber

    def addRoom(self, room):
        self.array.append(room)

    def printRooms(self):
        print("Anthill Room Array:")
        print("Ant number :", self.getAntNumber())
        for r in self.array:
            r.printRoom()

    def printTunnels(self):
        print(self.matrice)

    def printAnthill(self):
        self.printRooms()
        print("Tunnels:")
        self.printTunnels()

    def addTunnel(self, firstRoom, secondRoom):
        self.matrice.append((firstRoom, secondRoom))








# Tunnels
# Sommets
# matriceInit(self):
#        self.matrice[0] = []
#        for r in self.array:
#            self.matrice[0].append(r.getName())
#        print("Sommets:", self.matrice[0])
