from tkinter import *
from datetime import datetime

window = Tk()
window.title("Age Calculator App")
window.geometry("400x400")

l1 = Label(window,text="Enter your name:",fg="black",bg="lightblue")
e1= Entry(window)
l1.place(x=50,y=50)
e1.place(x=250,y=50)

l2 = Label(window,text="Enter your birth date:",fg="black",bg="lightpink")
e2= Entry(window)
l2.place(x=50,y=100)
e2.place(x=250,y=100)

l3 = Label(window,text="Enter your birth month:",fg="black",bg="lightgreen")
e3= Entry(window)
l3.place(x=50,y=150)
e3.place(x=250,y=150)

l4 = Label(window,text="Enter your birth year:",fg="black",bg="yellow")
e4= Entry(window)
l4.place(x=50,y=200)
e4.place(x=250,y=200)

def msg():
    user_name = (e1.get())
    birth_date = int(e2.get())
    birth_month = int(e3.get())
    birth_year = int(e4.get())

    today = datetime.now()

    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_date))
    personalised_msg = f"Hello {user_name}. Your age is {age}."
    t1.insert(END, personalised_msg)

btn = Button(window,text="Calculate Current Age",fg="black",bg="grey",command=msg)
btn.place(x=250,y=250)

text = Label(window,text="Note: Please enter values for birth date and birth month in numeric form.")
text.place(x=1,y=300)


t1= Text(window,height='4')
t1.pack(side=BOTTOM)

window.mainloop()