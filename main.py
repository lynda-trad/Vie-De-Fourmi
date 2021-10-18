# Fourmi
from os.path import exists

import Room
import Anthill


# 1 - Lecture du fichier txt choisi pour determiner :
# taille de la fourmiliere + nombre de salles en plus de Sd et Sv

def fileParsing(anthill):
    filename = 'fourmiliere_quatre.txt'
    while not exists(filename):
        filename = input("Please enter a filename.\n")

    file = open(filename, "r")
    lines = file.readlines()
    antNumber = lines.pop(0)  # line one is always the number of ants
    print(antNumber)

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

    if not capacity.isdigit():
        print("Error, capacity has to be a digit, please check the file again, capacity will be default size 1")
        capacity = ""

    return capacity


def roomInit(line):
    # Creates a room
    name = line[0] + line[1]
    r = Room.Room(name, 1)
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
