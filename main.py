# Fourmi
from os.path import exists
import numpy
import Room
import Anthill
import Ant
import fileParsing


def printStep(stepIndex):
    st = ""
    st += "+++ E" + stepIndex + " +++"
    # print only if there is a movement between rooms


anthil = Anthill.Anthill()
# Adjacency matrix
matrix = fileParsing.fileParsing(anthil)

# Debugging
anthil.printAnthill()
print(matrix)

stepIndex = 1
