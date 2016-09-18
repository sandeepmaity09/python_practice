import tkinter as tk
from tkinter import Menu

win=tk.Tk()
win.title("Python GUI")

menuBar=Menu(win)
win.config(menu=menuBar)


def _quit():
    win.quit()
    win.destroy()
    exit()
    
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Exit",command=_quit)
menuBar.add_cascade(label="File",menu=fileMenu)

helpMenu=Menu(menuBar)
helpMenu.add_command(label="Help")
helpMenu.add_command(label="About us")
menuBar.add_cascade(label="Help",menu=helpMenu)

