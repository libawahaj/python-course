from tkinter import *

window = Tk()
window.title('Length Converter App')
window.geometry('400x400')

l1 = Label(window,text='Converting Inch to Cm',fg='black',bg='lightblue')
l1.pack(side=TOP)

l2 = Label(window,text='Enter the value in inches you want to convert:',fg='black',bg='lightpink')
l2.place(x=75,y=60)

e1= Entry(window)
e1.place(x=130,y=130)

def converter():
    value = int(e1.get())
    cm_value= value*2.54
    text = f"{value} inches is {cm_value} cm."
    t1.insert(END,text)

b1 = Button(window,text='Convert!',fg='black',bg='lightgreen',command=converter)
b1.place(x=160,y=180)

t1= Text(window,height=6)
t1.place(x=1,y=250)

window.mainloop()