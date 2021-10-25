from os.path import exists

import networkx as nx

import Anthill
import fileParsing
import networkx as nx
import matplotlib.pyplot


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

# NetworkX Graph init
G = nx.Graph()
G.add_node('Sv')
G.add_node('Sd')
for node in anthil.getRoomArray():
    name = node.getName()
    G.add_node(name)
for edge in anthil.getTunnel():
    G.add_edge(edge[0], edge[1])

# Printing NetworkX Graph init
nx.draw(G, with_labels=True, font_size=8, alpha=0.8, node_color="#A86CF3")
print(G)
# use function nex.annotate to put current number of ants above its cell


stepIndex = 1
if len(matrix) != 0:
    print("---Travel result ---\n")
    finalStep = travel(matrix, stepIndex, anthil)
    print(finalStep)
    print("All the ants can sleep now !")
else:
    print("matrix is not initialized correctly, please check the file again")
