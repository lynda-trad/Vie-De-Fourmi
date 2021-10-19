from os.path import exists
import numpy
import Room
import Anthill
import Ant
import fileParsing


def printStep(stepId):
    st = ""
    st += "+++ E" + stepId + " +++"
    # print only if there is a movement between rooms


def moveToNextRoom(currentLocation, currentAnt, anthil, matrix):
    for j in range(len(matrix[currentLocation])):
        if matrix[currentLocation][j] == 1:
            currentRoom = anthil.returnRoomWithIndex(currentLocation)
            nextRoom = anthil.returnRoomWithIndex(j)
            if nextRoom.canEnter():
                currentRoom.setCapacityLeft(False)
                nextRoom.setCapacityLeft(True)
                currentAnt.setLocation(nextRoom)


def allInSd(anthil):
    allInSd = True
    for f in range(anthil.getAntArray()):
        if anthil.antArray[f].getLocation() != 1:
            allInSd = False
    return allInSd


def travel(matrix, stepId, anthill):
    # Etape numero stepIndex
    # toutes les fourmis commencent à Sv = 1
    # on regarde dans la matrice sur la ligne 1, la premiere case == 1
    # on prend cet index et on deplace la fourmi la bas
    # fourmi.setLocation = j
    # on change capacity de room index j avec True
    # on change capacity de room index i avec False
    for f in range(anthill.getAntArray()):
        currentAnt = anthill.antArray[f]
        currentLocation = currentAnt.getLocation()
        if currentLocation != 1:  # if ant is not in Sd
            moveToNextRoom(currentLocation, currentAnt, anthil, matrix)

    stepId += 1
    if not allInSd():
        travel(matrix, stepId, anthill)
    return


###########################################################
anthil = Anthill.Anthill()
# Adjacency matrix
matrix = fileParsing.fileParsing(anthil)

# Debugging
anthil.printAnthill()
print(matrix)

stepIndex = 1

travel(matrix, stepIndex, anthil)
