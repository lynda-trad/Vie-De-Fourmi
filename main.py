# Fourmi
from os.path import exists

import Room
import Anthill


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


def fileParsing(anthill):
    filename = 'fourmiliere_quatre.txt'
    while not exists("./ressources/" + filename):
        filename = input("Please enter a filename.\n")

    file = open("./ressources/" + filename, "r")
    lines = file.readlines()

    antLine = lines.pop(0)  # line one is always the number of ants
    antNumber = getAntNumber("", antLine)
    if antNumber == "":  # Error : ant number is not a number
        return
    anthill.setAntNumber(int(antNumber))

    # Adds Sd and Sv rooms to Anthill Array
    Sd = Room.Room("Sd", int(antNumber))
    Sv = Room.Room("Sv", int(antNumber))
    anthill.addRoom(Sd)
    anthill.addRoom(Sv)

    for line in lines:
        # Tunnel
        if '-' in line:
            tunnelsInit(line, anthill)
        else:  # Room
            anthill.addRoom(roomInit(line))


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


def roomInit(line):
    # Creates a room
    name = line[0] + line[1]
    capacity = getRoomCapacity("", line)
    if len(capacity) == 0:
        r = Room.Room(name, 1)
    else:
        r = Room.Room(name, int(capacity))
    r.printRoom()
    return r


def tunnelsInit(line, anthill):
    # Creates a tunnel between two rooms
    space = ""
    print(space.isspace())

    firstRoom = ""
    secondRoom = ""
    i = 0
    while line[i] != '-':
        if not line[i].isspace() or line[i] != '\n' or line[i] != "":
            firstRoom += line[i]
        else:
            print("line[i] is a space")
        print("character", i, ":", line[i])
        i += 1
    # We are at character '-'
    i += 2
    while line[i] != '\n':
        if not line[i].isspace() or line[i] != '\n' or line[i] != "":
            secondRoom += line[i]
        else:
            print("line[i] is a space")
        print("character", i, ":", line[i])
        i += 1

    # if firstRoom in anthill.getArray() and secondRoom in anthill.getArray():
    anthill.addTunnel(firstRoom, secondRoom)


# 2 - initialisation de la fourmiliere

anthill = Anthill.Anthill()
fileParsing(anthill)

anthill.printAnthill()
