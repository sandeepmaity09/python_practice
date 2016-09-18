import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox
win=tk.Tk()
win.title("Python GUI")

menuBar=Menu(win)
win.config(menu=menuBar)


def _quit():
    win.quit()
    win.destroy()

def _msgbox():
    mBox.showinfo('Python Message Info Box','A python GUI created using tkinter:\nThe Year is 2016.')

def _msgboxwarn():
    mBox.showwarning('Python Message Warning Box','A python GUI created using tkinter:\nWarning : There might be a bug in the code.')
    
def _msgboxerr():
    mBox.showerror('Python Message Erroe Box','A Python GUI created using tkinter:\n Error: Huston: we have a serious PROBLEM!')

def _msgboxchose():
    answer=mBox.askyesno("Python Message Dual Choice Box",'Are you really sure to do this?')
    print(answer)
    
fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label="Exit",command=_quit)
menuBar.add_cascade(label="File",menu=fileMenu)

helpMenu=Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=_msgbox)
helpMenu.add_command(label="Warning",command=_msgboxwarn)
helpMenu.add_command(label="Error",command=_msgboxerr)
helpMenu.add_command(label="Choose",command=_msgboxchose)
menuBar.add_cascade(label="Help",menu=helpMenu)
