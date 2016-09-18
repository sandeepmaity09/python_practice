import tkinter as tk
win=tk.Tk()
strData=tk.StringVar()
strData.set("Hello StringVar")
varData=strData.get()
print(varData)

integer=tk.IntVar()
double=tk.DoubleVar()
boolean=tk.BooleanVar()

print(integer.get())
print(double.get())
print(boolean.get())
