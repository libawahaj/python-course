from tkinter import *

window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

l1 = Label(window, text="Multiplication Calculator", fg="black", bg="lightblue")
l1.pack()

l2 = Label(window,text="Enter your first number:", fg="black", bg="lightpink")
l2.pack()

e1= Entry(window) 
e1.pack()

l3 = Label(window,text="Enter your second number:", fg="black", bg="lightpink")
l3.pack()

e2= Entry(window) 
e2.pack()

def calc():
    fn = float(e1.get())
    sn = float(e2.get())
    value = fn*sn
    msg = "The product is: ", value
    t1.insert(END, msg)

b1 = Button(window, text="Calculate",fg="black",bg="lightgreen", command=calc)
b1.pack()

t1= Text(window,height='4')
t1.pack()

window.mainloop()