# -*- coding: utf-8 -*-
from InputFile import *
from GraphComposer import *


def main(y1Path, y2Path, title, xText, y1Text, y2Text, checkVar):
    inpFile = InputFile(y1Path, y2Path)
    inpFile.parseValues()
    generalDataArray = inpFile.returnData()
    generalUnitsArray = inpFile.units()
    generalPathsArray = inpFile.pathsToFiles()
    y1PathsArray = generalPathsArray[0]
    y2PathsArray = generalPathsArray[1]

    for eachElement in y1PathsArray:
        print(eachElement)
    for eachElement in y2PathsArray:
        print(eachElement)

    y1UnitsArray = generalUnitsArray[0]
    y2UnitsArray = generalUnitsArray[1]
    graph = GraphComposer(checkVar)
    graph.text(title, xText, y1Text, y2Text)
    graph.setup(y1UnitsArray[0], y1UnitsArray[1], y2UnitsArray[1])

    i = int(0)
    while (i < 2):
        yArray = generalDataArray[i]
        if (i == 0):
            z = int(0)
            while (z < len(yArray)):
                currentYArray = yArray[z]
                graph.addY1Data(currentYArray[1], currentYArray[0], y1PathsArray[z])
                z += 1
        elif (i == 1):
            print(i)
            x = int(0)
            while (x < len(yArray)):
                currentYArray = yArray[x]
                graph.addY2Data(currentYArray[1], currentYArray[0], y2PathsArray[x])
                x += 1
        i += 1

    graph.plotData()
