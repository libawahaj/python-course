from tkinter import *

window = Tk()
window.title("Main Window")
window.geometry('500x500')

def toplevel():
    toplevel = Toplevel()
    toplevel.title("Top Level Window")
    toplevel.geometry("200x200")

    l1 = Label(toplevel,text="This is the top level window", bg= 'lightgrey', fg='black')
    l1.pack()

    toplevel.mainloop()

b1 = Button(window, text = "Click here to add top window", command=toplevel)
b1.pack()

window.mainloop()