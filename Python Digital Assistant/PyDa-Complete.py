from Tkinter import *
import wolframalpha
import wikipedia
root=Tk()

#function that takes gets executed when the submit button is pressed
def getinput():
    top=Toplevel()              #window which pops up as soon as the button is pressed
    global entry
    answer = StringVar()
    ques=entry.get()            #getting the input in ques using the get function
    try:
        #wolframalpha
        app_id = "PTXV4K-QRKQLHW54H"
        client = wolframalpha.Client(app_id)
        res = client.query(ques)
        answer.set(next(res.results).text)

    except:
        #wikipedia
        answer.set(wikipedia.summary(ques).encode('utf-8'))
    label=Label(top, textvariable=answer, wraplength=600, justify=LEFT)     #putting the value of the answer in the label
    label.pack(side=BOTTOM)

#****************** GUI *********************
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