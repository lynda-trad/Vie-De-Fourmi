import time
from os.path import exists

import networkx as nx
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import Anthill
import fileParsing
import networkx as nx
import matplotlib.pyplot as plt


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


def travel(graph, nodePos, matrix, stepId, anthil):
    step = ""
    printGraph(graph, nodePos, anthil)
    while not allInSd(anthil):
        step += "+++ E" + str(stepId) + " +++\n"
        for f in range(len(anthil.getAntArray())):
            currentAnt = anthil.antArray[f]
            currentLocation = currentAnt.getLocation()

            if int(currentLocation) != 0:  # if ant is not in Sd
                step = moveToNextRoom(int(currentLocation), currentAnt, anthil, matrix, step)
        printGraph(graph, nodePos, anthil)
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
    return graph, nodePos


# Printing NetworkX Graph
def printGraph(graph, nodePos, anthil):
    figure = plt.gcf()
    figure.canvas.manager.set_window_title('Anthill')
    figure.canvas.manager.window.SetPosition = (500, 500)

    nx.draw(graph, nodePos, with_labels=True, font_size=8, alpha=0.8, node_color="#A86CF3")
    for room in anthil.getRoomArray():
        room.printRoom()
        currentName = room.getName()
        currentCapacity = room.getMaxCapacity() - room.getCapacityLeft()
        x, y = pos[currentName]
        plt.text(x, y + 0.1, s=currentCapacity, bbox=dict(facecolor='red', alpha=0.5), horizontalalignment='center')

    plt.savefig("anthill.png")
    plt.draw()
    plt.pause(1)
    figure.clear()
    plt.clf()  # clear figure from the canvas


###########################################################
anthil = Anthill.Anthill()
# Adjacency matrix
matrix = fileParsing.fileParsing(anthil)

# Debugging
print("Adjacency matrix:\n", matrix)
anthil.printAnthill()

# NetworkX Graph init
G, pos = initPrintingGraph(anthil)

stepIndex = 1
if len(matrix) != 0:
    print("---Travel result ---\n")
    finalStep = travel(G, pos, matrix, stepIndex, anthil)
    print(finalStep)
    print("All the ants can sleep now !")
else:
    print("matrix is not initialized correctly, please check the file again")
