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
    filename = 'fourmiliere_cinq.txt'
    while not exists(filename):
        filename = input("Please enter a filename.\n")

    file = open(filename, "r")
    lines = file.readlines()

    antLine = lines.pop(0)  # line one is always the number of ants
    antNumber = getAntNumber("", antLine)
    if antNumber == "":   # Error : ant number is not a number
        return
    anthill.setAntNumber(int(antNumber))

    # Add Sd and Sv rooms to Anthill Array
    Sd = Room.Room("Sd", int(antNumber))
    Sv = Room.Room("Sv", int(antNumber))
    anthill.addRoom(Sd)
    anthill.addRoom(Sv)

    for line in lines:
        # If line has a '-' it means its a line about tunnels between two rooms
        if '-' in line:
            tunnelsInit(line)
        else:  # else its a room initialisation
            anthill.addRoom(roomInit(line))
        print(line)


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


def tunnelsInit(line):
    # Creates a tunnel between two rooms
    return


# 2 - initialisation de la fourmiliere

anthill = Anthill.Anthill()
fileParsing(anthill)

anthill.printRooms()
