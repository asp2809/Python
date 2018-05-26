from tkinter import *
import re

root=Tk()
root.configure(background='#00001a')
root.geometry("1000x350+300+300")
root.title("Regular Expression Validator")

regex=StringVar()
ex=StringVar()
answer=StringVar()

#functions definitions
def validate():
    regex1=regex.get()
    example=ex.get()
    try:
        if re.match(regex1, example):
            regexvalid=re.compile(regex1)
            ans=regexvalid.findall(example)
            ansstr="Matches:"
            for i in ans:
                ansstr+="\t"+i
            answer.set(ansstr)
        else:
            answer.set("No matches")
    except:
        answer.set("Invalid Regular Expression")

#creating buttons, labels and entries
labelhead=Label(root, text="Regex Validator", font="Arial 25 bold underline", width=50, height=2, fg="#00001a", bg="#ffcc99")
labelhead.grid(columnspan=2)
label1=Label(root, text="Regular Expression: ", padx=5, pady=20, font="Arial 18", bg="#00001a", fg="#ffcc99")
label1.grid(row=1, column=0)
entryreg=Entry(root, textvariable=regex, font="Arial 18", bg="#ffcc99")
entryreg.grid(row=1, column=1)
label2=Label(root, text="Test Example: ", padx=5, pady=5,  font="Arial 18", bg="#00001a", fg="#ffcc99")
label2.grid(row=2, column=0)
entryex=Entry(root, textvariable=ex, font="Arial 18", bg="#ffcc99")
entryex.grid(row=2, column=1)
anslabel=Label(root, textvariable=answer, width=50, font="Arial 16", fg="#ffcc99", bg="#00001a", pady=15)
submit=Button(root, text="Submit", command=validate, font="Arial 18", bg="#ffcc99", width=10)
exitbtn=Button(root, text="Exit", command=root.destroy, font="Arial 18", bg="#ffcc99", width=10)
anslabel.grid(columnspan=2)
submit.grid(row=4, column=0)
exitbtn.grid(row=4, column=1)

root.mainloop()