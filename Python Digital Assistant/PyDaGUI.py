from Tkinter import *
root=Tk()

def getinput():
    pass

root.geometry("350x80+300+300")
label=Label(root, text="Hi! I am your Python Digital Assistant. How can I help you today?")
entry=Entry(root)
submit=Button(root, text="Submit", bg="light green", command=getinput)

exit1=Button(root, text="Exit", bg="red", fg="white", command=root.destroy)

label.pack()
entry.pack(fill=X)
entry.focus_set()
submit.pack(side=LEFT)
exit1.pack(side=LEFT)
root.mainloop()