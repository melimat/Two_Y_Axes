import matplotlib.pyplot as plt

class GraphComposer:

	def __init__(self):
		self.fig, self.ax1 = plt.subplots()
	def text(self, titl, xText, y1Text, y2Text):
		self.titl = titl
		self.xText = xText
		self.y1Text = y1Text
		self.y2Text = y2Text
	def setup(self, xUnits, y1Units, y2Units):
		color = 'red'
		plt.title(self.titl)
		self.ax1.set_xlabel(self.xText + " ["+ xUnits+"]")
		self.ax1.set_ylabel(self.y1Text + " ["+y1Units +"]", color=color)
		self.ax2 = self.ax1.twinx()
		color = "blue"
		self.ax2.set_ylabel(self.y2Text + " ["+y2Units+"]", color=color)
	def addY1Data(self, y1Data, timeArray, nameOfFile):
		color = "red"
		self.ax1.plot(timeArray, y1Data, label = nameOfFile, color = color)
		self.ax1.tick_params(axis='y', labelcolor=color)
	def addY2Data(self, y2Data, timeArray, nameOfFile):
		color = "blue"
		self.ax2.plot(timeArray, y2Data, label = nameOfFile, color = color)
		self.ax2.tick_params(axis='y', labelcolor=color)
	def plotData(self):
		self.fig.tight_layout()
		plt.show()