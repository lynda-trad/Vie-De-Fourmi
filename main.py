import time
from os.path import exists

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Anthill
import fileParsing
import networkx as nx
import matplotlib.pyplot as plt


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
    allInSd = True
    for f in range(len(anthill.getAntArray())):
        if anthill.antArray[f].getLocation() != 0:
            allInSd = False
    return allInSd


# Ant travel
def travel(graph, nodePos, stepId, anthill, paths):
    step = ""
    printGraph(graph, nodePos, anthill, stepId - 1)
    while not allInSd(anthill):
        step += "+++ E" + str(stepId) + " +++\n"
        for f in range(len(anthill.getAntArray())):
            currentAnt = anthill.antArray[f]
            currentLocation = currentAnt.getLocation()

            if int(currentLocation) != 0:  # if ant is not in Sd
                step = moveToNextRoom(currentLocation, currentAnt, anthill, step, paths)
        printGraph(graph, nodePos, anthill, stepId)
        stepId += 1
    time.sleep(5)
    return step


# Init Graph with Networkx
def initPrintingGraph(anthill):
    graph = nx.Graph()
    graph.add_node('Sv')
    graph.add_node('Sd')
    # Add nodes = rooms
    for node in anthill.getRoomArray():
        name = node.getName()
        graph.add_node(name)
    # Add edges = tunnels
    for edge in anthill.getTunnel():
        graph.add_edge(edge[0], edge[1])

    nodePos = nx.spring_layout(graph)
    nx.draw(graph, nodePos, with_labels=True, font_size=8, alpha=0.8, node_color="#A86CF3")
    plt.savefig("./steps/anthill.png")
    return graph, nodePos


# Printing NetworkX Graph
def printGraph(graph, nodePos, anthill, stepId):
    figure = plt.gcf()
    figure.canvas.manager.set_window_title('Anthill')
    figure.canvas.manager.window.SetPosition = (200, 200)

    nx.draw(graph, nodePos, with_labels=True, font_size=8, alpha=0.8, node_color="#A86CF3")
    for room in anthill.getRoomArray():
        currentName = room.getName()
        currentCapacity = room.getMaxCapacity() - room.getCapacityLeft()
        x, y = pos[currentName]
        plt.text(x, y + 0.1, s=currentCapacity, bbox=dict(facecolor='red', alpha=0.5), horizontalalignment='center')

    plt.savefig("./steps/step" + str(stepId) + ".png")
    plt.draw()
    plt.pause(1)
    figure.clear()
    plt.clf()  # clear figure from the canvas


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
G, pos = initPrintingGraph(anthil)

possiblePaths = bestTravel(adjacencyMatrix)
print("\n Possible path: ", possiblePaths, "\n")

stepIndex = 1
if len(adjacencyMatrix) != 0:
    finalStep = travel(G, pos, adjacencyMatrix, stepIndex, anthil, possiblePaths)
    print("---Travel result ---\n")
    print(finalStep)
    print("All the ants can sleep now !")
else:
    print("matrix is not initialized correctly, please check the file again")
