import time
import Anthill
import fileParsing
import graphPrinting


def moveToNextRoom(currentLocation, currentAnt, anthill, step, paths):
    moved = False
    currentRoom = anthill.returnRoomWithIndex(int(currentLocation))

    for i in range(len(paths)):
        if int(currentLocation) in paths[i] and not moved:
            nextLocation = paths[i][paths[i].index(int(currentLocation)) + 1]
            nextRoom = anthill.returnRoomWithIndex(nextLocation)
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


# Checks if all of the ants are in Sd
def allInSd(anthill):
    allInside = True
    for f in range(len(anthill.getAntArray())):
        if anthill.antArray[f].getLocation() != 0:
            allInside = False
    return allInSd


# Ant travel
def travel(graph, nodePos, stepId, anthill, paths):
    step = ""
    graphPrinting.printGraph(graph, nodePos, anthill, stepId - 1)
    while not allInSd(anthill):
        step += "+++ E" + str(stepId) + " +++\n"
        for f in range(len(anthill.getAntArray())):
            currentAnt = anthill.antArray[f]
            currentLocation = currentAnt.getLocation()

            if int(currentLocation) != 0:
                step = moveToNextRoom(currentLocation, currentAnt, anthill, step, paths)
        graphPrinting.printGraph(graph, nodePos, anthill, stepId)
        stepId += 1
    time.sleep(5)
    return step


# Calculates the best path to go from Sv to Sd
def bestTravel(matrix):
    startingPossibilities = []
    pathPossibilities = []
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            startingPossibilities.append(i)
    for p in startingPossibilities:
        start = p
        path = [start]
        while start != 1:
            for i in range(len(matrix)):
                if matrix[i][start] == 1:
                    start = i
                    path.insert(0, i)
        path.append(0)
        pathPossibilities.append(path)
    return pathPossibilities


###########################################################
anthil = Anthill.Anthill()

adjacencyMatrix = fileParsing.fileParsing(anthil)
print("Adjacency matrix:\n", adjacencyMatrix)
anthil.printAnthill()

# NetworkX Graph init
G, pos = graphPrinting.initPrintingGraph(anthil)

possiblePaths = bestTravel(adjacencyMatrix)
print("\n Possible path: ", possiblePaths, "\n")

stepIndex = 1
if len(adjacencyMatrix) != 0:
    finalStep = travel(G, pos, stepIndex, anthil, possiblePaths)
    print("---Travel result ---\n")
    print(finalStep)
    print("All the ants can sleep now !")
else:
    print("matrix is not initialized correctly, please check the file again")
