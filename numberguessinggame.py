#program of a number guessing game
from tkinter import *
from random import randint
import tkinter.messagebox

root=Tk()
#initializing the size and the position of the window
root.geometry("200x100+300+300")
global nes
#generating a random number between 0 and 9 both inclusive
nes=randint(0,9)
#program to check the guessed number and then displaying whether it is greater or smaller than the generated number or the user has guessed it correct
def check():
    global e
    global p
    n=int(e.get())
    if(nes<n):
        p="Greater!"
    elif(nes>n):
        p="Smaller!"
    else:
        p="You got it right!!"
    tkinter.messagebox.showinfo("info name", p)

#Making the GUI
label=Label(root, text="Number Guessing Game")
label.pack(side=TOP, fill=X)
label1=Label(root, text="Enter any number(0-9)")
label1.pack(fill=X)
e=Entry(root)
e.pack()
e.focus_set()

#when the user presses the submit button then the check function is called and if the exit button is pressed then the program exits
submit=Button(root, text="Submit", fg="green", command=check)
submit.pack(side=LEFT)
Clear=Button(root, text="Exit", fg="red", command=root.destroy)
Clear.pack(side=RIGHT)

root.mainloop()