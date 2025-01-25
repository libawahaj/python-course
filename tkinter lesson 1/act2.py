from tkinter import *
from datetime import date

window = Tk()
window.title("Activity 2")
window.geometry('500x500')

l1 = Label(window,text='Hello there', fg='black', bg='lightblue')
l1.pack()
l2= Label(window,text='Enter your full name', fg='black', bg='lightpink')
l2.pack()

e1 = Entry(window)
e1.pack()

def dis():
    g = "hello " + e1.get()
    m = " welcome to the application \n, today's date is "
    t1.insert(END,g)
    t1.insert(END,m)
    t1.insert(END,date.today())


b1 = Button(window, text='begin', fg = 'black',bg="blue",command=dis)
b1.pack()

t1= Text(window,height='4')
t1.pack()

window.mainloop()

