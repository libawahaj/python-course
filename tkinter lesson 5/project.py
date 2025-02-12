from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Strength Checker App")
window.geometry('400x400')
window.configure(bg="lightgrey")


def top():
    topwin = Toplevel()
    topwin.geometry('300x300')
    topwin.title("Password Strength Checker")

    l2 = Label(topwin, text="Enter your password here:", bg="lightblue", fg="black")
    l2.pack()
    
    e1 = Entry(topwin, show="*") 
    e1.pack()

    def checker():
        password = e1.get()
        length = len(password)
        points = 0

        if any(char.islower() for char in password):
            points += 1

        if any(char.isupper() for char in password):
            points += 1

        if any(char.isdigit() for char in password):
            points += 1

        if any(not char.isalnum() for char in password):
            points += 1

        
        if length <= 5:
            points += 0 
        elif 6 <= length <= 8:
            points += 1
        elif 9 <= length <= 12:
            points += 2
        else:
            points += 3


        if points <= 3:
            messagebox.showinfo("Password Strength", "Your password is TOO WEAK!")
        elif points == 4:
            messagebox.showinfo("Password Strength", "Your password has MODERATE strength.")
        elif points == 5:
            messagebox.showinfo("Password Strength", "Your password is STRONG.")
        elif points >= 6:
            messagebox.showinfo("Password Strength", "Your password is VERY STRONG!")


    btn = Button(topwin, text="Check Strength", bg="pink", fg="black", command=checker)
    btn.pack()


l1 = Label(window, text="Hello User! Welcome to the Password Strength Checker App.", bg="darkgrey", fg="black")
l1.place(x=35, y=150)

b1 = Button(window, text="Let's get Started!", bg="grey", fg="black", command=top)
b1.place(x=150, y=200)

window.mainloop()
