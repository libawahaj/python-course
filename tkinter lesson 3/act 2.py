from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Alert")
window.geometry('200x200')

def msg():
    messagebox.showwarning('Alert!',"Virus has been detected")

b1 = Button(window,text="Scan for Virus", command=msg)
b1.pack()

window.mainloop()