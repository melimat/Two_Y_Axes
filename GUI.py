# -*- coding: utf-8 -*-
from main import *

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

def GUI():
	root = Tk()

	y1PathEntry = Entry(root)
	y2PathEntry = Entry(root)
	titleEntry = Entry(root)
	xLabelEntry = Entry(root)
	y1LabelEntry = Entry(root)
	y2LabelEntry = Entry(root)

	def y1DirPick():
		y1PathEntry.delete(0, "end")
		root.y1DirPath = tkFileDialog.askdirectory(initialdir="/",title="Select directory")
		y1PathEntry.insert(10, root.y1DirPath)
	def y2DirPick():
		y2PathEntry.delete(0, "end")
		root.y2DirPath = tkFileDialog.askdirectory(initialdir="/",title="Select directory")
		y2PathEntry.insert(10, root.y2DirPath)
	def generate():
		y1Path = y1PathEntry.get()
		y2Path = y2PathEntry.get()
		Title = titleEntry.get()
		XLabel = xLabelEntry.get()
		Y1Label = y1LabelEntry.get()
		Y2Label = y2LabelEntry.get()
		root.destroy()
		main(y1Path, y2Path, Title, XLabel, Y1Label, Y2Label)

	y1PickButton = Button(root, text = "...", command = y1DirPick)
	y2PickButton = Button(root, text = "...", command = y2DirPick)
	okButton = Button(root, text = "OK", command = generate)

	y1PathEntryLabel = Label(root, text = "Path to Y1 data: ", height = 4)
	y2PathEntryLabel = Label(root, text = "Path to Y2 data: ", height = 4)
	titleEntryLabel = Label(root, text = "Title for graph: ", height = 4)
	xLabelEntryLabel = Label(root, text = "X Axis label: ", height = 4)
	y1LabelEntryLabel = Label(root, text = "Y1 Axis label: ", height = 4)
	y2LabelEntryLabel = Label(root, text = "Y2 Axis label: ", height = 4)

	y1PathEntryLabel.grid(row = 0, column = 0)
	y2PathEntryLabel.grid(row = 1, column = 0)
	titleEntryLabel.grid(row = 2, column = 0)
	xLabelEntryLabel.grid(row = 3, column = 0)
	y1LabelEntryLabel.grid(row = 4, column = 0)
	y2LabelEntryLabel.grid(row = 5, column = 0)

	y1PathEntry.grid(row = 0, column = 1)
	y2PathEntry.grid(row = 1, column = 1)
	titleEntry.grid(row = 2, column = 1)
	xLabelEntry.grid(row = 3, column = 1)
	y1LabelEntry.grid(row = 4, column = 1)
	y2LabelEntry.grid(row = 5, column = 1)

	y1PickButton.grid(row = 0, column = 2)
	y2PickButton.grid(row = 1, column = 2)
	okButton.grid(row = 6, column = 1)

	root.mainloop()

GUI()