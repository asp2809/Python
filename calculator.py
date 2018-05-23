from tkinter import *
from math import *

root=Tk()
ex=""

var=StringVar()

#functions to manipulate the expression and result
#function which gets exebuted on the click of any digit or . button which adds the parameter to the expression and then configures the label
def btnclick(btnr):
    global ex
    ex+=btnr['text']
    var.set(ex)
    label.config(textvariable=var)

#function which gets executed on the = button click which evaluates the expression using the eval function and then updates the value in both label and the expresssion
def equalclick():
    global ex
    try:
        ans=eval(ex)
        var.set(ans)
        label.config(textvariable=var)
        ex=str(ans)
    except:
        #if any error occurs then the except block prints the following text in label2
        label2.config(text="Error!! Invalid Input")

#function to clear all the inputs which is done by clearing the expression and updating the value in label
def allclear():
    global ex
    ex=""
    var.set(ex)
    label.config(textvariable=var)
    
#function to clear only the last character entered which gets executed when the C button is pressed
def clear():
    global ex
    ex=ex[0:len(ex)-1]
    var.set(ex)
    label.config(textvariable=var)

#creating all the labels, buttons and entries
label=Label(root, textvariable=var, bg="#b3cccc", width=25, height=1, anchor="e")
label2=Label(root, text="", bg="#b3cccc", fg="red", width=25, height=1, anchor="e")
label.grid(columnspan=4)
label2.grid(columnspan=4)
bracket1=Button(root, text="(", width=5, height=2, bg="#d580ff", command=lambda: btnclick(bracket1))
bracket1.grid(row=2, column=2)
bracket2=Button(root, text=")", width=5, height=2, bg="#d580ff", command=lambda: btnclick(bracket2))
bracket2.grid(row=2, column=3)
btnac=Button(root, text="AC", width=5, height=2, bg="#ff5050", command=allclear)
btnac.grid(row=2, column=0)
btnc=Button(root, text="C", width=5, height=2, bg="#ff5050", command=clear)
btnc.grid(row=2, column=1)
btn1=Button(root, text="7", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn1))
btn1.grid(row=3, column=0)
btn2=Button(root, text="8", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn2))
btn2.grid(row=3, column=1)
btn3=Button(root, text="9", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn3))
btn3.grid(row=3, column=2)
btn4=Button(root, text="/", width=5, height=2, bg="#ff9933", command=lambda: btnclick(btn4))
btn4.grid(row=3, column=3)
btn5=Button(root, text="4", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn5))
btn5.grid(row=4, column=0)
btn6=Button(root, text="5", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn6))
btn6.grid(row=4, column=1)
btn7=Button(root, text="6", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn7))
btn7.grid(row=4, column=2)
btn8=Button(root, text="*", width=5, height=2, bg="#ff9933", command=lambda: btnclick(btn8))
btn8.grid(row=4, column=3)
btn9=Button(root, text="1", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn9))
btn9.grid(row=5, column=0)
btn10=Button(root, text="2", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn10))
btn10.grid(row=5, column=1)
btn11=Button(root, text="3", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn11))
btn11.grid(row=5, column=2)
btn12=Button(root, text="-", width=5, height=2, bg="#ff9933", command=lambda: btnclick(btn12))
btn12.grid(row=5, column=3)
btn13=Button(root, text="0", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn13))
btn13.grid(row=6, column=0)
btn14=Button(root, text=".", width=5, height=2, bg="#1a66ff", command=lambda: btnclick(btn14))
btn14.grid(row=6, column=1)
btn15=Button(root, text="=", width=5, height=2, bg="#80ff80", command=equalclick)
btn15.grid(row=6, column=2)
btn16=Button(root, text="+", width=5, height=2, bg="#ff9933", command=lambda: btnclick(btn))
btn16.grid(row=6, column=3)

root.mainloop()