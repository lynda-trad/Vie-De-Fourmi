from os.path import exists
import numpy
import Room
import Anthill
import Ant


# Parses line 0 to find ant number specified like this : f=10
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


# Initializes anthill's ant array with antNumber x Ant objects
def antNumberInit(lines, anthill):
    antLine = lines.pop(0)  # line one is always the number of ants
    antNumber = getAntNumber("", antLine)
    if antNumber == "":  # Error : ant number is not a number
        print("Error, ant number \'f\' has to be a digit, please check the file again")
        return
    anthill.setAntNumber(int(antNumber))
    anthill.addAnts()
    return antNumber


# Initializes Sd and Sv room objects in anthill room array
def sd_sv_init(antNumber, anthill):
    # Adds Sd and Sv rooms to Anthill Array
    Sd = Room.Room("Sd", int(antNumber), 0)
    Sv = Room.Room("Sv", int(antNumber), 1)
    Sd.setCapacityLeft(int(antNumber))
    Sv.setCapacityLeft(0)
    anthill.addRoom(Sd)
    anthill.addRoom(Sv)


# Parses line to find if room capacity is specified like this S1 { 2 }
def getRoomCapacity(capacity, line):
    if '{' in line:
        try:
            idx1 = line.index("{")
            idx2 = line.index("}")
            for idx in range(idx1 + 2, idx2):
                capacity += str(line[idx])
            n = int(capacity)
        except ValueError:
            print("Error, capacity has to be digit, capacity will be default size 1, please check the file again")
            capacity = ""
    return capacity


# Creates a room object with parsed line
def roomInit(line, index):
    # Creates a room
    name = line[0] + line[1]
    capacity = getRoomCapacity("", line)
    if len(capacity) == 0:
        r = Room.Room(name, 1, index)
    else:
        r = Room.Room(name, int(capacity), index)
    return r


# Initializes Anthill's tunnels list like this [(S1, S2), (S2, S3), ...]
def tunnelsInit(line, anthill):
    firstRoom = ""
    secondRoom = ""
    try:
        words = line.split()
        firstRoom = words[0]
        # '-' = words[1]
        secondRoom = words[2]
    except ValueError:
        print("Error, tunnel is not initialized correctly, please check the file again")
    roomNames = anthill.getRoomNames()
    if firstRoom in roomNames and secondRoom in roomNames:
        anthill.addTunnel(firstRoom, secondRoom)


# Initializes adjacency matrix in main.py with anthill's tunnels and room indexes
def initMatrix(anthill):
    if anthill.getLength() == 0:
        print("Error, there are no rooms, so no matrix, please check file again")
        return
    matrix = numpy.zeros((anthill.getLength(), anthill.getLength()))
    for tup in anthill.getTunnel():
        room_zero = anthill.returnRoomWithName(tup[0])
        room_one = anthill.returnRoomWithName(tup[1])
        matrix[room_zero.getIndex()][room_one.getIndex()] = 1
    return matrix


# File parsing launcher
def fileParsing(anthill):
    filename = input("Please enter a filename with txt extension from folder /ressources.\n")
    while not exists("./ressources/" + filename):
        filename = input("Please enter a valid filename.\n")

    file = open("./ressources/" + filename, "r")
    lines = file.readlines()

    antNumber = antNumberInit(lines, anthill)

    sd_sv_init(antNumber, anthill)
    index = 2

    for line in lines:
        if '-' in line:  # Tunnel
            tunnelsInit(line, anthill)
        else:            # Room
            room = roomInit(line, index)
            anthill.addRoom(room)
            index += 1

    return initMatrix(anthill)
