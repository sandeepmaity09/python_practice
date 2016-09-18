import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("CheckBox")

check1var=tk.IntVar()
check1=tk.Checkbutton(win,text="Disabled",variable=check1var,state='disabled')
check1.select()
check1.grid(column=0,row=0,sticky=tk.W)
check2var=tk.IntVar()
check2=tk.Checkbutton(win,text="Disabled",variable=check2var,state='disabled')
check2.deselect()
check3var=tk.IntVar()
check3=tk.Checkbutton(win,text="Select",variable=check3var)
check3.select()
check4var=tk.Tk()
check4=tk.Checkbutton(win,text="Unselect",variable=check4var)
check4.deselect()


check2.grid(column=0,row=1,sticky=tk.W)
check3.grid(column=0,row=2,sticky=tk.W)
check4.grid(column=0,row=3,sticky=tk.W)

