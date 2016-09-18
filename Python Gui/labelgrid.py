import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

nameLabel=ttk.Label(win,text="Enter Your Name: ")
numberLabel=ttk.Label(win,text="Choose a Number: ")
namevar=tk.StringVar()
numbervar=tk.StringVar()
nameEnt=ttk.Entry(win,width=12,textvariable=namevar)
numberCom=ttk.Combobox(win,width=12,textvariable=numbervar)

nameLabel.grid(column=0,row=0)
numberLabel.grid(column=1,row=0)
nameEnt.grid(column=0,row=1)
numberCom.grid(column=1,row=1)

labelsFrame=ttk.LabelFrame(win,text="Label's in frame")
labelsFrame.grid(column=0,row=4,padx=20,pady=40)
ttk.Label(labelsFrame,text="Label1").grid(column=0,row=0)
ttk.Label(labelsFrame,text="Label2").grid(column=1,row=0)
ttk.Label(labelsFrame,text="Label3").grid(column=2,row=0)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8,pady=4)
