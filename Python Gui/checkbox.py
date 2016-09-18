import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("CheckBox")

aLabel=ttk.Label(win,text="Enter a name:")
aLabel.grid(column=0,row=0)

bLabel=ttk.Label(win,text="Choose a Number:")
bLabel.grid(column=1,row=0)

name=tk.StringVar()
aEntry=ttk.Entry(win,width=12,textvariable=name)
aEntry.grid(column=0,row=1)

number=tk.StringVar()
aComboBox=ttk.Combobox(win,width=12,textvariable=number)
aComboBox['values']=(1,2,3,4,5)
aComboBox.grid(column=1,row=1)
aComboBox.current(2)

def clickMe():
    pass

aButton=ttk.Button(win,text="Click Me!",command=clickMe)
aButton.grid(column=3,row=1)

dis=tk.IntVar()
aCheckBox=tk.Checkbutton(win,text="Disabled",variable=dis,state='disabled')
aCheckBox.select()
aCheckBox.grid(column=0,row=2,sticky=tk.W)

uncheck=tk.IntVar()
bCheckBox=tk.Checkbutton(win,text="UnChecked",variable=uncheck)
bCheckBox.deselect()
bCheckBox.grid(column=1,row=2,sticky=tk.W)

check=tk.IntVar()
cCheckBox=tk.Checkbutton(win,text="Checked",variable=check)
cCheckBox.select()
cCheckBox.grid(column=3,row=2,sticky=tk.W)

