import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("DETAILS")

name=tk.StringVar()
aLabel=ttk.Label(win,text="Choose a Number : ")
aEntry=ttk.Entry(win,width=8,textvariable=name)
aComboBox=ttk.Combobox(win,width=12,textvariable=name,state='readonly')
aComboBox['values']=(1,2,3,5,76)
aLabel.grid(column=0,row=0)
aEntry.grid(column=1,row=0)
aComboBox.grid(column=2,row=0)
aLab=ttk.Label(win,text="")

def click():
    aLab.configure(text="You Choose The Number : "+name.get())

    
aBut=ttk.Button(win,text="Submit",command=click)
aBut.grid(column=3,row=0)
aLab.grid(column=0,row=1)
