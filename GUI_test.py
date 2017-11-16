import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
filename = tkFileDialog.askopenfile()
print(filename)



