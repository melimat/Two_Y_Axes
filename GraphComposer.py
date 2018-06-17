import matplotlib.pyplot as plt


class GraphComposer:

    def __init__(self, checkVar):
        self.fig, self.ax1 = plt.subplots()
        self.lineStyles = ["-", "--", "-.", ":"]
        self.checkVar = checkVar
        self.numberOfLines1 = int(0)
        self.numberOfLines2 = int(0)

    def text(self, titl, xText, y1Text, y2Text):
        self.titl = titl
        self.xText = xText
        self.y1Text = y1Text
        self.y2Text = y2Text

    def setup(self, xUnits, y1Units, y2Units):
        color = 'red'
        plt.title(self.titl)
        self.ax1.set_xlabel(self.xText + " [" + xUnits + "]")
        self.ax1.set_ylabel(self.y1Text + " [" + y1Units + "]", color=color)
        self.ax2 = self.ax1.twinx()
        color = "blue"
        self.ax2.set_ylabel(self.y2Text + " [" + y2Units + "]", color=color)

    def addY1Data(self, y1Data, timeArray, pathToFile):
        if (self.checkVar == 1):
            self.numberOfLines1 += 1
            currentLineStyle = self.lineStyles[self.numberOfLines1 - 1]
            if(self.numberOfLines1 == 4):
                self.numberOfLines1 = 0
        else:
            currentLineStyle=self.lineStyles[0]

        color = "red"
        pathArray = pathToFile.split("/")
        nameOfFile = "Source: " + pathArray[len(pathArray)-1]
        self.ax1.plot(timeArray, y1Data, label=nameOfFile, color=color, linestyle=currentLineStyle)
        self.ax1.tick_params(axis='y', labelcolor=color)

    def addY2Data(self, y2Data, timeArray, pathToFile):
        if (self.checkVar == 1):
            self.numberOfLines2 += 1
            currentLineStyle = self.lineStyles[self.numberOfLines2 - 1]
            if (self.numberOfLines2 == 4):
                self.numberOfLines2 = 0
        else:
            currentLineStyle=self.lineStyles[0]

        color = "blue"
        pathArray = pathToFile.split("/")
        nameOfFile = "Source: " + pathArray[len(pathArray) - 1]
        self.ax2.plot(timeArray, y2Data, label=nameOfFile, color=color, linestyle=currentLineStyle)
        self.ax2.tick_params(axis='y', labelcolor=color)

    def plotData(self):
        self.fig.tight_layout()
        self.ax1.legend(loc="upper left")
        self.ax2.legend(loc="upper right")
        plt.show()