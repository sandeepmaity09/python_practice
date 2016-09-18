import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Combo Box")

aLabel=ttk.Label(win,text="Choose a Number:")
aLabel.grid(column=0,row=0)

def clickMe():
    aButton.configure(text="I'm Clicked")
    aLabel.configure(text="Hello"+number.get(),foreground='blue')

aButton=ttk.Button(win,text="Click Me!",command=clickMe)
aButton.grid(column=2,row=1)

name=tk.StringVar()
aEntry=ttk.Entry(win,width=12,textvariable=name)
aEntry.grid(column=0,row=1)

number=tk.StringVar()
aComboBox=ttk.Combobox(win,width=12,textvariable=number,state='readonly')
aComboBox['values']=(1,2,3,4,5,6)
aComboBox.grid(column=1,row=1)
aComboBox.current(0)

