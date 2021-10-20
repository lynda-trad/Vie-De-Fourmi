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
                currentRoom.antMovement(False)
                nextRoom.antMovement(True)
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
    step = ""
    while not allInSd(anthil):
        step += "+++ E" + str(stepId) + " +++\n"
        for f in range(len(anthil.getAntArray())):
            currentAnt = anthil.antArray[f]
            currentLocation = currentAnt.getLocation()
            if int(currentLocation) != 0:  # if ant is not in Sd
                step = moveToNextRoom(int(currentLocation), currentAnt, anthil, matrix, step)
        stepId += 1
    return step


###########################################################
anthil = Anthill.Anthill()
# Adjacency matrix
matrix = fileParsing.fileParsing(anthil)

# Debugging
print("Adjacency matrix:\n", matrix)
anthil.printAnthill()

stepIndex = 1
if len(matrix) != 0:
    print("---Travel result ---\n")
    finalStep = travel(matrix, stepIndex, anthil)
    print(finalStep)
    print("All the ants can sleep now !")
else:
    print("matrix is not initialized correctly, please check the file again")
