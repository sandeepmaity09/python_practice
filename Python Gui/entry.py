import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Entry")

aLabel=ttk.Label(win,text="Enter Your Name:")
aLabel.grid(column=0,row=0)

def clickMe():
    aButton.configure(text="Hello"+name.get())
    aLabel.configure(foreground='blue',text="Hello"+name.get())

aButton=ttk.Button(win,text="Click Me!",command=clickMe)
aButton.grid(column=1,row=1)
aButton.configure(state='disabled')

name=tk.StringVar()
aEntry=ttk.Entry(win,textvariable=name)
aEntry.grid(column=0,row=1)
aEntry.focus()
win.mainloop()

