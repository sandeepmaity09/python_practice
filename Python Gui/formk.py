import tkinter as tk
from tkinter import ttk


win=tk.Tk()
win.title("Details")
fnameLab=ttk.Label(win,text="Enter Your First Name: ")
lnameLab=ttk.Label(win,text="Enter Your Last Name: ")
detailsLab=ttk.Label(win,text="")
fname=tk.StringVar()
lname=tk.StringVar()
fnameEnt=ttk.Entry(win,width=12,textvariable=fname)
lnameEnt=ttk.Entry(win,width=12,textvariable=lname)
def click():
    detailsLab.configure(text="Your Name is "+fname.get()+" "+lname.get())

detButton=ttk.Button(win,text="Submit",command=click)

fnameLab.grid(column=0,row=0)
fnameEnt.grid(column=1,row=0)
lnameLab.grid(column=0,row=1)
lnameEnt.grid(column=1,row=1)
detButton.grid(column=0,row=2)
detailsLab.grid(column=0,row=3)

win.resizable(40,40)
win.mainloop()
    
