import networkx as nx
import matplotlib.pyplot as plt


# Inits Graph with Networkx
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
    drawNodes(anthill, nodePos, graph)
    drawNamesAndCapacities(anthill, nodePos)
    plt.savefig("./steps/anthill.png")
    plt.tight_layout()
    plt.axis("off")
    return graph, nodePos


# Draws room names and their capacities above nodes
def drawNamesAndCapacities(anthill, nodePos):
    for room in anthill.getRoomArray():
        currentName = room.getName()
        currentCapacity = room.getMaxCapacity() - room.getCapacityLeft()
        x, y = nodePos[currentName]
        plt.text(x, y - 0.025, s=currentName, horizontalalignment='center')
        plt.text(x, y + 0.1, s=currentCapacity, bbox=dict(facecolor='red', alpha=0.5), horizontalalignment='center')


# Draws node in different colors
def drawNodes(anthill, nodePos, graph):
    roomNames = anthill.getRoomNames()
    roomNames.remove('Sd')
    roomNames.remove('Sv')
    nx.draw_networkx_nodes(graph, nodePos, nodelist=['Sd'], node_color="#119617")
    nx.draw_networkx_nodes(graph, nodePos, nodelist=['Sv'], node_color="#FF5511")
    nx.draw_networkx_nodes(graph, nodePos, nodelist=roomNames, node_color="#FCE205")
    nx.draw_networkx_edges(graph, nodePos, width=1.0, alpha=0.5)


# Prints NetworkX Graph
def printGraph(graph, nodePos, anthill, stepId):
    figure = plt.gcf()
    figure.canvas.manager.set_window_title('Anthill')
    figure.canvas.manager.window.SetPosition = (200, 200)
    drawNodes(anthill, nodePos, graph)
    drawNamesAndCapacities(anthill, nodePos)
    plt.savefig("./steps/step" + str(stepId) + ".png")
    plt.tight_layout()
    plt.axis("off")
    plt.draw()
    plt.pause(1)
    figure.clear()
    plt.clf()
