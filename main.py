# Fourmi
from os.path import exists

import numpy

import Room
import Anthill
import Ant


# 1 - Lecture du fichier txt choisi pour determiner :
# taille de la fourmiliere + nombre de salles en plus de Sd et Sv
def getAntNumber(number, line):
    for i in range(2, len(line)):
        if line[i] != '\n':
            number += line[i]
        try:
            n = int(number)
        except ValueError:
            print("Error, ant number \'f\' has to be a digit, please check the file again")
            number = ""
    return number


def antNumberInit(lines, anthill):
    antLine = lines.pop(0)  # line one is always the number of ants
    antNumber = getAntNumber("", antLine)
    if antNumber == "":  # Error : ant number is not a number
        print("Error, ant number \'f\' has to be a digit, please check the file again")
        return
    anthill.setAntNumber(int(antNumber))
    anthill.addAnts()
    return antNumber


def sd_sv_init(antNumber, anthill):
    # Adds Sd and Sv rooms to Anthill Array
    Sd = Room.Room("Sd", int(antNumber), 0)
    Sv = Room.Room("Sv", int(antNumber), 1)
    anthill.addRoom(Sd)
    anthill.addRoom(Sv)


def fileParsing(anthill):
    filename = 'fourmiliere_quatre.txt'
    while not exists("./ressources/" + filename):
        filename = input("Please enter a filename.\n")

    file = open("./ressources/" + filename, "r")
    lines = file.readlines()

    antNumber = antNumberInit(lines, anthill)

    sd_sv_init(antNumber, anthill)
    index = 2

    for line in lines:
        # Tunnel
        if '-' in line:
            tunnelsInit(line, anthill)
        else:  # Room
            anthill.addRoom(roomInit(line, index))
            index += 1

    anthill.printAnthill()
    return initMatrix(anthill)


def getRoomCapacity(capacity, line):
    if line[2] != '\n':
        if line[3] == '{':
            for i in range(4, len(line)):
                if line[i] != '}':
                    capacity += line[i]
        try:
            n = int(capacity)
        except ValueError:
            print("Error, capacity has to be a digit, please check the file again, capacity will be default size 1")
            capacity = ""
    return capacity


def roomInit(line, index):
    # Creates a room
    name = line[0] + line[1]
    capacity = getRoomCapacity("", line)
    if len(capacity) == 0:
        r = Room.Room(name, 1, index)
    else:
        r = Room.Room(name, int(capacity), index)
    r.printRoom()
    return r


def tunnelsInit(line, anthill):
    # Creates a tunnel between two rooms
    firstRoom = ""
    secondRoom = ""
    try:
        words = line.split()
        firstRoom = words[0]
        # '-' = words[1]
        secondRoom = words[2]
    except ValueError:
        print("Error, tunnel is not initialized correctly, please check the file again")
    roomNames = anthill.getNames()
    if firstRoom in roomNames and secondRoom in roomNames:
        anthill.addTunnel(firstRoom, secondRoom)


def initMatrix(anthill):
    print("\n MATRIX INIT \n")
    if anthill.getLength() == 0:
        print("Error, there are no rooms, so no matrix, please check file again")
        return
    matrice = numpy.zeros((anthill.getLength(), anthill.getLength()))
    for tup in anthill.getTunnel():
        room_zero = anthill.returnRoom(tup[0])
        room_one = anthill.returnRoom(tup[1])
        matrice[room_zero.getIndex()][room_one.getIndex()] = 1
        matrice[room_one.getIndex()][room_zero.getIndex()] = 1
    return matrice


# 2 - initialisation de la fourmiliere

anthill = Anthill.Anthill()
# Adjacency matrix
matrix = fileParsing(anthill)

# Debugging
anthill.printAnthill()
print(matrix)

f_one = Ant.Ant("F1", "Sd")
f_one.printAnt()
