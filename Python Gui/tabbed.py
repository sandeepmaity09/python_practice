import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win=tk.Tk()
win.title("Python GUI")
tabControl=ttk.Notebook(win)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Tab1')
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='Tab2')
tabControl.pack(expand=1,fill="both")

monty=ttk.LabelFrame(tab1,text="Monty Python")
monty.grid(column=0,row=0,padx=8,pady=4)

nameLabel=ttk.Label(monty,text="Enter a name: ")
name=tk.StringVar()
nameEntry=ttk.Entry(monty,width=12,textvariable=name)
nameLabel.grid(column=0,row=0,padx=8,pady=4)
nameEntry.grid(column=0,row=1,padx=8,pady=4)

numberLabel=ttk.Label(monty,text="Enter a Number: ")
number=tk.StringVar()
numberCombo=ttk.Combobox(monty,width=12,textvariable=number,state='readonly')
numberCombo['values']=(1,2,3,4,5)
numberCombo.current(4)
numberCombo.grid(column=1,row=1,padx=8,pady=4)
numberLabel.grid(column=1,row=0,padx=8,pady=4)

def clickMe():
    pass

submitButton=ttk.Button(monty,text="Submit",command=clickMe)
submitButton.grid(column=2,row=1,padx=8,pady=4)

dis=tk.IntVar()
disCheck=tk.Checkbutton(monty,text="Disabled",variable=dis,state='disabled')
disCheck.select()
disCheck.grid(column=0,row=3,padx=8,pady=4)

uncheck=tk.IntVar()
uncheckCheck=tk.Checkbutton(monty,text="Select",variable=uncheck)
uncheckCheck.select()
uncheckCheck.grid(column=1,row=3,padx=8,pady=4)

check=tk.IntVar()
checkCheck=tk.Checkbutton(monty,text="Toogle",variable=check)
checkCheck.deselect()
checkCheck.grid(column=2,row=3,padx=8,pady=4)




python=ttk.LabelFrame(tab2,text="The Snake")
python.grid(column=1,row=1,padx=8,pady=4)


COLOR1="blue"
COLOR2="red"
COLOR3="green"

radval=tk.IntVar()
def redCall():
    redsel=radval.get()
    if redsel==1:
        win.configure(background=COLOR1)
    elif redsel==2:
        win.configure(background=COLOR2)
    elif redsel==3:
        win.configure(background=COLOR3)


rad1=tk.Radiobutton(python,text=COLOR1,variable=radval,value=1,command=redCall)
rad1.grid(column=0,row=0,padx=8,pady=4)

rad2=tk.Radiobutton(python,text=COLOR2,variable=radval,value=2,command=redCall)
rad2.grid(column=1,row=0,padx=8,pady=4)

rad3=tk.Radiobutton(python,text=COLOR3,variable=radval,value=3,command=redCall)
rad3.grid(column=2,row=0,padx=8,pady=4)

sc=scrolledtext.ScrolledText(python,width=30,height=10,wrap=tk.WORD)
sc.grid(column=0,columnspan=3,padx=8,pady=4)


win.mainloop()
