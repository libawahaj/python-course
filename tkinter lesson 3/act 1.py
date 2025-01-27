from tkinter import *

window = Tk()
window.title('Events in Tkinter')
window.geometry('100x100')

def handle_keypress(event):
    print(event.char)

def handle_msg(event):
    print('\n The button was clicked!')

button = Button(text='Click me!')
button.pack()

button.bind('<Button-1>', handle_msg)

window.mainloop()