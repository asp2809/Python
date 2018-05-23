#program for restaurant management system using tkinter
from tkinter import *
import datetime

root=Tk()
root.title("Restaurant Management System")
root.geometry("1000x500+200+200")
now=datetime.datetime.now()
var = []
for i in range(8):
    el=StringVar()
    var.append(el)
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
label=Label(root, text="Restaurant Management System", font="Arial 20 bold underline", padx=280, pady=10, fg="#0066cc")
label.grid(columnspan=4)
labeldate=Label(root, text=now.strftime("%d-%m-%Y").center(80, "-"), font="Arial 18 bold italic", fg="#0066cc")
labeldate.grid(columnspan=4)

#first row
var[0].set("1")
label1=Label(root, text="Order No.", width=10, height=3, font="Verdana 14", fg="#0066cc")
label1.grid(row=2, column=0)
label2=Label(root, text="Drinks", width=10, height=3, font="Verdana 14", fg="#0066cc")
label2.grid(row=2, column=2)
entry1=Entry(root, textvariable=var[0], font="Verdana 14", bg="#ffcc99")
entry1.grid(row=2, column=1)
entry2=Entry(root, textvariable=var[1], font="Verdana 14", bg="#ffcc99")
entry2.grid(row=2, column=3)

#second row
label3=Label(root, text="Cheese Burger", width=11, height=3, font="Verdana 14", fg="#0066cc")
label3.grid(row=3, column=0)
label4=Label(root, text="Cost", width=10, height=3, font="Verdana 14", fg="#0066cc")
label4.grid(row=3, column=2)
entry3=Entry(root, textvariable=var[2], font="Verdana 14", bg="#ffcc99")
entry3.grid(row=3, column=1)
entry4=Entry(root, textvariable=var[3], font="Verdana 14", bg="#ffcc99")
entry4.grid(row=3, column=3)

#third row
label5=Label(root, text="French Fries", width=10, height=3, font="Verdana 14", fg="#0066cc")
label5.grid(row=4, column=0)
label6=Label(root, text="GST", width=10, height=3, font="Verdana 14", fg="#0066cc")
label6.grid(row=4, column=2)
entry5=Entry(root, textvariable=var[4], font="Verdana 14", bg="#ffcc99")
entry5.grid(row=4, column=1)
entry6=Entry(root, textvariable=var[5], font="Verdana 14", bg="#ffcc99")
entry6.grid(row=4, column=3)

#fourth row
label7=Label(root, text="Econo Meals", width=10, height=3, font="Verdana 14", fg="#0066cc")
label7.grid(row=5, column=0)
label8=Label(root, text="TOTAL", width=10, height=3, font="Verdana 14", fg="#0066cc")
label8.grid(row=5, column=2)
entry7=Entry(root, textvariable=var[6], font="Verdana 14", bg="#ffcc99")
entry7.grid(row=5, column=1)
entry8=Entry(root, textvariable=var[7], font="Verdana 14", bg="#ffcc99")
entry8.grid(row=5, column=3)

#fifth row
button1=Button(root, text="Price List", command=listprice, width=16, height=3, font="Helvetica 12 bold", bg="#ffcc99")
button1.grid(row=6, column=0)
button2=Button(root, text="Total Amount", command=calculate, width=16, height=3, font="Helvetica 12 bold", bg="#ffcc99")
button2.grid(row=6, column=1)
button3=Button(root, text="Next Order", command=reset, width=16, height=3, font="Helvetica 12 bold" , bg="#ffcc99")
button3.grid(row=6, column=2)
button4=Button(root, text="Exit", command=root.destroy, width=16, height=3, font="Helvetica 12 bold", bg="#ffcc99")
button4.grid(row=6, column=3)

root.mainloop()