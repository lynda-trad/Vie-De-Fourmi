import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import matplotlib.pyplot as plt


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
        x, y = nodePos[currentName]
        plt.text(x, y + 0.1, s=currentCapacity, bbox=dict(facecolor='red', alpha=0.5), horizontalalignment='center')

    plt.savefig("./steps/step" + str(stepId) + ".png")
    plt.draw()
    plt.pause(1)
    figure.clear()
    plt.clf()
