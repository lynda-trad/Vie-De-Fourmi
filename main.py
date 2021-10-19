from os.path import exists
import numpy
import Room
import Anthill
import Ant
import fileParsing


def moveToNextRoom(currentLocation, currentAnt, anthil, matrix, step):
    moved = False
    currentRoom = anthil.returnRoomWithIndex(currentLocation)
    for j in range(len(matrix)):
        if matrix[currentLocation][j] == 1 and not moved:
            nextRoom = anthil.returnRoomWithIndex(j)
            if nextRoom.canEnter():
                print("\nBefore move")
                print("Current Room")
                currentRoom.printRoom()
                print("Next Room")
                nextRoom.printRoom()

                currentRoom.antMovement(False)
                nextRoom.antMovement(True)

                print("\nAfter move")
                print("Current Room")
                currentRoom.printRoom()
                print("Next Room")
                nextRoom.printRoom()

                currentAnt.setLocation(nextRoom.getIndex())
                step += currentAnt.getName() + " - "
                step += currentRoom.getName() + " - "
                step += nextRoom.getName() + "\n"
                moved = True
                return step
    return step


def allInSd(anthil):
    allInSd = True
    for f in range(len(anthil.getAntArray())):
        if anthil.antArray[f].getLocation() != 0:
            allInSd = False
    return allInSd


def travel(matrix, stepId, anthil):
    step = "+++ E" + str(stepId) + " +++\n"

    while not allInSd(anthil):
        for f in range(len(anthil.getAntArray())):
            currentAnt = anthil.antArray[f]
            print("\ncurrentAnt:")
            currentAnt.printAnt()
            currentLocation = currentAnt.getLocation()
            if int(currentLocation) != 0:  # if ant is not in Sd
                step = moveToNextRoom(int(currentLocation), currentAnt, anthil, matrix, step)
        stepId += 1
        print(step)

    print(step)
    return step


###########################################################
anthil = Anthill.Anthill()
# Adjacency matrix
matrix = fileParsing.fileParsing(anthil)

# Debugging
print(matrix)
anthil.printAntArray()
#anthil.printAnthill()

stepIndex = 1
#finalStep = travel(matrix, stepIndex, anthil)