#program for Restaurant Management System with calculator using tkinter
from tkinter import *
import datetime
from math import *

root=Tk()

#frame for the restaurant management part
frame1=Frame(root, width=1000, height=1000, padx=20, pady=20)
#frame for the calculator part
frame2=Frame(root, width=700, height=1000, padx=50, pady=20, highlightcolor="#000", highlightthickness="3", bd=0)
root.title("Restaurant Management System")
now=datetime.datetime.now()
label=Label(root, text="Restaurant Management System", font="Arial 20 bold underline", padx=280, pady=10, fg="#0066cc")
label.pack()
labeldate=Label(root, text=now.strftime("%d-%m-%Y").center(80, "-"), font="Arial 18 bold italic", fg="#0066cc")
labeldate.pack()
var = []
for i in range(8):
    el=StringVar()
    var.append(el)
ex=""

var1=StringVar()

#********************Part 1-Restaurant Management System Part****************************
#functions definitions
#function to be called when "Price List" button is pressed
def listprice():
    top=Toplevel()
    top.title("Price List")
    top.geometry("300x150+150+150")
    labelhead1=Label(top, text="Items", fg="#990000", padx=50, pady=5, font="Sans-serif 12 bold underline")
    labelhead2=Label(top, text="Price", fg="#990000", padx=50, pady=5, font="Sans-serif 12 bold underline")
    labelhead1.grid(row=0, column=0)
    labelhead2.grid(row=0, column=1)
    labelip3=Label(top, text="Cheese Burger")
    labelip4=Label(top, text="₹ 60")
    labelip3.grid(row=1, column=0)
    labelip4.grid(row=1, column=1)
    labelip5=Label(top, text="French Fries")
    labelip6=Label(top, text="₹ 40")
    labelip5.grid(row=2, column=0)
    labelip6.grid(row=2, column=1)
    labelip7=Label(top, text="Drinks")
    labelip8=Label(top, text="₹ 60")
    labelip7.grid(row=3, column=0)
    labelip8.grid(row=3, column=1)
    labelip9=Label(top, text="Econo Meal")
    labelip10=Label(top, text="₹ 120")
    labelip9.grid(row=4, column=0)
    labelip10.grid(row=4, column=1)

#function which will be called when "Total" button is pressed
def calculate():
    amt=0
    l=[1,2,4,6]
    for i in l:
        if var[i].get()!="":
            if i==1 or i==2:
                amt+=(int(var[i].get())*60)
            elif i==4:
                amt+=(int(var[i].get())*40)
            elif i==6:
                amt+=(int(var[i].get())*120)
    gst=0.05*amt
    totalamt=amt+gst
    var[3].set(str(amt))
    var[5].set(str(gst))
    var[7].set(str(totalamt))
    entry4.config(textvariable=var[3])
    entry6.config(textvariable=var[5])
    entry8.config(textvariable=var[7])

#function which will be called on the pressing of "Reset" button
def reset():
    for i in range(1,8):
        var[i].set("")
    entry2.config(textvariable=var[1])
    entry3.config(textvariable=var[2])
    entry4.config(textvariable=var[3])
    entry5.config(textvariable=var[4])
    entry6.config(textvariable=var[5])
    entry7.config(textvariable=var[6])
    entry8.config(textvariable=var[7])
    var[0].set(str(int(var[0].get())+1))
    entry1.config(textvariable=var[0])

#creating labels, buttons and entries

#first row
var[0].set("1")
label1=Label(frame1, text="Order No.", width=10, height=3, font="Verdana 14", fg="#0066cc")
label1.grid(row=2, column=0)
label2=Label(frame1, text="Drinks", width=10, height=3, font="Verdana 14", fg="#0066cc")
label2.grid(row=2, column=2)
entry1=Entry(frame1, textvariable=var[0], font="Verdana 14", bg="#ffcc99")
entry1.grid(row=2, column=1)
entry2=Entry(frame1, textvariable=var[1], font="Verdana 14", bg="#ffcc99")
entry2.grid(row=2, column=3)

#second row
label3=Label(frame1, text="Cheese Burger", width=11, height=3, font="Verdana 14", fg="#0066cc")
label3.grid(row=3, column=0)
label4=Label(frame1, text="Cost", width=10, height=3, font="Verdana 14", fg="#0066cc")
label4.grid(row=3, column=2)
entry3=Entry(frame1, textvariable=var[2], font="Verdana 14", bg="#ffcc99")
entry3.grid(row=3, column=1)
entry4=Entry(frame1, textvariable=var[3], font="Verdana 14", bg="#ffcc99")
entry4.grid(row=3, column=3)

#third row
label5=Label(frame1, text="French Fries", width=10, height=3, font="Verdana 14", fg="#0066cc")
label5.grid(row=4, column=0)
label6=Label(frame1, text="GST", width=10, height=3, font="Verdana 14", fg="#0066cc")
label6.grid(row=4, column=2)
entry5=Entry(frame1, textvariable=var[4], font="Verdana 14", bg="#ffcc99")
entry5.grid(row=4, column=1)
entry6=Entry(frame1, textvariable=var[5], font="Verdana 14", bg="#ffcc99")
entry6.grid(row=4, column=3)

#fourth row
label7=Label(frame1, text="Econo Meals", width=10, height=3, font="Verdana 14", fg="#0066cc")
label7.grid(row=5, column=0)
label8=Label(frame1, text="TOTAL", width=10, height=3, font="Verdana 14", fg="#0066cc")
label8.grid(row=5, column=2)
entry7=Entry(frame1, textvariable=var[6], font="Verdana 14", bg="#ffcc99")
entry7.grid(row=5, column=1)
entry8=Entry(frame1, textvariable=var[7], font="Verdana 14", bg="#ffcc99")
entry8.grid(row=5, column=3)

#fifth row
button1=Button(frame1, text="Price List", command=listprice, width=16, height=3, font="Helvetica 12 bold", bg="#ffcc99")
button1.grid(row=6, column=0)
button2=Button(frame1, text="Total Amount", command=calculate, width=16, height=3, font="Helvetica 12 bold", bg="#ffcc99")
button2.grid(row=6, column=1)
button3=Button(frame1, text="Next Order", command=reset, width=16, height=3, font="Helvetica 12 bold" , bg="#ffcc99")
button3.grid(row=6, column=2)
button4=Button(frame1, text="Exit", command=root.destroy, width=16, height=3, font="Helvetica 12 bold", bg="#ffcc99")
button4.grid(row=6, column=3)

frame1.pack(side=LEFT)
#********************Part 1-Restaurant Management System Part Ending****************************

#********************Part 2-Calculator Part****************************

#functions to manipulate the expression and result
#function which gets exebuted on the click of any digit or . button which adds the parameter to the expression and then configures the label
def btnclick(btnr):
    global ex
    ex+=btnr['text']
    var1.set(ex)
    lbl.config(textvariable=var1)

#function which gets executed on the = button click which evaluates the expression using the eval function and then updates the value in both label and the expresssion
def equalclick():
    global ex
    try:
        ans=eval(ex)
        var.set(ans)
        lbl.config(textvariable=var1)
        ex=str(ans)
    except:
        #if any error occurs then the except block prints the following text in label2
        lbl2.config(text="Error!! Invalid Input")

#function to clear all the inputs which is done by clearing the expression and updating the value in label
def allclear():
    global ex
    ex=""
    var.set(ex)
    lbl.config(textvariable=var1)
    
#function to clear only the last character entered which gets executed when the C button is pressed
def clear():
    global ex
    ex=ex[0:len(ex)-1]
    var.set(ex)
    lbl.config(textvariable=var1)

#creating all the labels, buttons and entries
lbl=Label(frame2, textvariable=var1, bg="#b3cccc", width=23, height=1, anchor="e", font="Helvetica 12 bold")
lbl2=Label(frame2, text="", bg="#b3cccc", fg="red", width=23, height=1, anchor="e", font="Helvetica 12 bold")
lbl.grid(columnspan=4)
lbl2.grid(columnspan=4)
bracket1=Button(frame2, text="(", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(bracket1), font="Helvetica 12 bold")
bracket1.grid(row=2, column=2)
bracket2=Button(frame2, text=")", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(bracket2), font="Helvetica 12 bold")
bracket2.grid(row=2, column=3)
btnac=Button(frame2, text="AC", width=5, height=2, bg="#ffcc99", command=allclear, font="Helvetica 12 bold")
btnac.grid(row=2, column=0)
btnc=Button(frame2, text="C", width=5, height=2, bg="#ffcc99", command=clear, font="Helvetica 12 bold")
btnc.grid(row=2, column=1)
btn1=Button(frame2, text="7", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn1), font="Helvetica 12 bold")
btn1.grid(row=3, column=0)
btn2=Button(frame2, text="8", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn2), font="Helvetica 12 bold")
btn2.grid(row=3, column=1)
btn3=Button(frame2, text="9", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn3), font="Helvetica 12 bold")
btn3.grid(row=3, column=2)
btn4=Button(frame2, text="/", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn4), font="Helvetica 12 bold")
btn4.grid(row=3, column=3)
btn5=Button(frame2, text="4", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn5), font="Helvetica 12 bold")
btn5.grid(row=4, column=0)
btn6=Button(frame2, text="5", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn6), font="Helvetica 12 bold")
btn6.grid(row=4, column=1)
btn7=Button(frame2, text="6", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn7), font="Helvetica 12 bold")
btn7.grid(row=4, column=2)
btn8=Button(frame2, text="*", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn8), font="Helvetica 12 bold")
btn8.grid(row=4, column=3)
btn9=Button(frame2, text="1", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn9), font="Helvetica 12 bold")
btn9.grid(row=5, column=0)
btn10=Button(frame2, text="2", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn10), font="Helvetica 12 bold")
btn10.grid(row=5, column=1)
btn11=Button(frame2, text="3", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn11), font="Helvetica 12 bold")
btn11.grid(row=5, column=2)
btn12=Button(frame2, text="-", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn12), font="Helvetica 12 bold")
btn12.grid(row=5, column=3)
btn13=Button(frame2, text="0", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn13), font="Helvetica 12 bold")
btn13.grid(row=6, column=0)
btn14=Button(frame2, text=".", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn14), font="Helvetica 12 bold")
btn14.grid(row=6, column=1)
btn15=Button(frame2, text="=", width=5, height=2, bg="#ffcc99", command=equalclick, font="Helvetica 12 bold")
btn15.grid(row=6, column=2)
btn16=Button(frame2, text="+", width=5, height=2, bg="#ffcc99", command=lambda: btnclick(btn), font="Helvetica 12 bold")
btn16.grid(row=6, column=3)

frame2.pack(side=LEFT)
#********************Part 2-Calculator Part Ending****************************


root.mainloop()