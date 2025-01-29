from tkinter import *

window = Tk()
window.title('Interest Calculator')
window.geometry("400x400")

l1 = Label(window, text="Calculating your interest", fg='black', bg='yellow')
l1.pack(side=TOP)

l2 = Label(window, text="Enter the principal amount", fg='black', bg='lightblue')
l2.place(x=20, y=50)

e1 = Entry(window)
e1.place(x=200, y=50)

l3 = Label(window, text="Enter the time in years", fg='black', bg='lightpink')
l3.place(x=20, y=90)

e2 = Entry(window)
e2.place(x=200, y=90)

l4 = Label(window, text="Enter the interest rate in %", fg='black', bg='lightgreen')
l4.place(x=20, y=130)

e3 = Entry(window)
e3.place(x=200, y=130)

def simple_interest():
    P = float(e1.get())
    t = float(e2.get())
    r = float(e3.get())
    SI = (P * t * r) / 100
    text = f"Your Simple Interest is {SI}"
    t1.insert(END, text + "\n")

def compound_interest():
    P = float(e1.get())
    t = float(e2.get())
    r = float(e3.get())
    A = P * (1 + r / 100) ** t
    CI = A - P
    text = f"Your Compound Interest is {CI}"
    t1.insert(END, text + "\n")

b1 = Button(window, text="Calculate Simple Interest", fg='black', bg="grey", command=simple_interest)
b1.place(x=20, y=170)

b2 = Button(window, text="Calculate Compound Interest", fg='black', bg="grey", command=compound_interest)
b2.place(x=200, y=170)

t1 = Text(window, height=5, width=45)
t1.place(x=20, y=220)

window.mainloop()