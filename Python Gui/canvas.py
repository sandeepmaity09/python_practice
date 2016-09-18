import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Python GUI")

tabControl=ttk.Notebook(win)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text="Tab 1")
tabControl.pack(expand=1,fill="both")

#adding the canvas

tab1=tk.Frame(tab1,bg="blue")
tab1.pack()
for orangeColor in range(2):
    canvas=tk.Canvas(tab1,width=150,height=80,highlightthickness=0,bg="orange")
    canvas.grid(row=orangeColor,column=orangeColor)

