import matplotlib.pyplot as plt
from random import choice


class GraphComposer:

    def __init__(self):
        self.fig, self.ax1 = plt.subplots()
        self.lineStyles = ["-", "--", "-.", ":"]
        self.usedLineStyles1 = []
        self.usedLineStyles2 = []

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

    def addY1Data(self, y1Data, timeArray, nameOfFile):
        while 1:
            currentLineStyle = choice(self.lineStyles)
            if(len(self.usedLineStyles1)>0):
                if (currentLineStyle in self.usedLineStyles1):
                    continue
                else:
                    break
                    self.usedLineStyles1.append(currentLineStyle)
            else:
                break
                self.usedLineStyles1.append(currentLineStyle)

        color = "red"
        self.ax1.plot(timeArray, y1Data, label=nameOfFile, color=color, linestyle = currentLineStyle)
        self.ax1.tick_params(axis='y', labelcolor=color)

    def addY2Data(self, y2Data, timeArray, nameOfFile):
        while 1:
            currentLineStyle = choice(self.lineStyles)
            if (len(self.usedLineStyles2) > 0):
                if (currentLineStyle in self.usedLineStyles2):
                    continue
                else:
                    break
                    self.usedLineStyles2.append(currentLineStyle)
            else:
                break
                self.usedLineStyles2.append(currentLineStyle)
        currentLineStyle = choice(self.lineStyles)
        color = "blue"
        self.ax2.plot(timeArray, y2Data, label=nameOfFile, color=color, linestyle = currentLineStyle)
        self.ax2.tick_params(axis='y', labelcolor=color)

    def plotData(self):
        self.fig.tight_layout()
        plt.show()
