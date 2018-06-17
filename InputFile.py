import os
import fnmatch


class InputFile:

    def __init__(self, y1DataFilesPath, y2DataFilesPath):
        self.y1DataFilesPathArr = []
        for file in os.listdir(y1DataFilesPath):
            if fnmatch.fnmatch(file, '*.txt'):
                self.y1DataFilesPathArr.append(y1DataFilesPath + "/" + file)
        self.y2DataFilesPathArr = []
        for file in os.listdir(y2DataFilesPath):
            if fnmatch.fnmatch(file, '*.txt'):
                self.y2DataFilesPathArr.append(y2DataFilesPath + "/" + file)

    def parseValues(self):
        self.y1UnitsArray = []
        self.y1GeneralDataArray = []
        firstOpened = bool(True)
        for eachElement in self.y1DataFilesPathArr:
            y1InputFile = open(eachElement, "r")
            i = int(0)
            y1GeneralInputArray = []
            timeArray = []
            dataArray = []
            for eachLine in y1InputFile:
                i += 1
                lineArray = eachLine.split("\t")
                if ((i == 6) and (firstOpened == True)):
                    self.y1UnitsArray.append(lineArray[0])
                    self.y1UnitsArray.append(lineArray[1])
                if (i >= 8):
                    timeArray.append(float(lineArray[0]))
                    dataArray.append(float(lineArray[1]))
            firstOpened = False
            y1GeneralInputArray.append(timeArray)
            y1GeneralInputArray.append(dataArray)
            self.y1GeneralDataArray.append(y1GeneralInputArray)

        self.y2UnitsArray = []
        self.y2GeneralDataArray = []
        firstOpened = True
        for eachElement in self.y2DataFilesPathArr:
            y1InputFile = open(eachElement, "r")
            i = int(0)
            y2GeneralInputArray = []
            timeArray = []
            dataArray = []
            for eachLine in y1InputFile:
                i += 1
                lineArray = eachLine.split("\t")
                if (i == 6) and (firstOpened == True):
                    self.y2UnitsArray.append(lineArray[0])
                    self.y2UnitsArray.append(lineArray[1])
                if (i >= 8):
                    timeArray.append(float(lineArray[0]))
                    dataArray.append(float(lineArray[1]))
            firstOpened = False
            y2GeneralInputArray.append(timeArray)
            y2GeneralInputArray.append(dataArray)
            self.y2GeneralDataArray.append(y2GeneralInputArray)

    def returnData(self):
        generalArray = []
        generalArray.append(self.y1GeneralDataArray)
        generalArray.append(self.y2GeneralDataArray)
        return (generalArray)

    def units(self):
        unitsArray = []
        unitsArray.append(self.y1UnitsArray)
        unitsArray.append(self.y2UnitsArray)
        return (unitsArray)
    def pathsToFiles(self):
        generalPathsArray = []
        generalPathsArray.append(self.y1DataFilesPathArr)
        generalPathsArray.append(self.y2DataFilesPathArr)
        return (generalPathsArray)
