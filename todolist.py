from tkinter import *
from random import randint

#initializing the root window and initializing the size of the window
root=Tk()
root.geometry("300x300+300+300")
root.title("To-do List App")
tasks=[]                                            #array to store the tasks

#function to update the list using the tasks
def update_item(tasks):
    listbox.delete(0, listbox.size()-1)
    for i in tasks:
        listbox.insert(listbox.size()+1, i)

#function to add a task
def add_item():
    global entry
    var=StringVar()
    var=entry.get()
    tasks.append(var)
    update_item(tasks)
    label3.config(text="Number of Tasks: " + str(len(tasks)))

#function to delete all the tasks
def delete_all():
    global tasks
    tasks=[]
    listbox.delete(0, listbox.size()-1)
    label3.config(text="Number of Tasks: " + str(len(tasks))) 
    label4.config(text="You can do: ")  

#function to choose an item at random from the tasks 
def choose_item():
    n=randint(0, len(tasks)-1)
    label4.config(text="You can do: " + tasks[n])

#function to sort the tasks in ascending order
def sort_asc():
    tasks.sort()
    update_item(tasks)

#function to sort the tasks in descending order
def sort_desc():
    tasks.sort()
    p=tasks[::-1]
    update_item(p)

#initializing the labels, listboxes and buttons
label=Label(root, text="To-Do List", padx=5, pady=5)
entry=Entry(root, bg="light yellow")
listbox=Listbox(root)
add_btn=Button(root, text="Add Task", bg="light green", command=add_item, pady=5)
deleteall_btn=Button(root, text="Delete All", bg="orange", command=delete_all)
choose_btn=Button(root, text="Random Selection", bg="sky blue", command=choose_item)
sort_asc=Button(root, text="Sort(ASC)", bg="yellow", command=sort_asc)
sort_desc=Button(root, text="Sort(DESC)", bg="yellow", command=sort_desc)
exit_btn=Button(root, text="Exit", bg="red", command=root.destroy, anchor=N)
label4=Label(root, text="You can do: ", pady=5)
label3=Label(root, text="Number of Tasks: " + str(len(tasks)), padx=50, pady=5)

#setting up the positions of the widgets
label.grid(columnspan=2)
deleteall_btn.grid(row=1, column=0)
choose_btn.grid(row=2, column=0)
sort_asc.grid(row=3, column=0)
sort_desc.grid(row=4, column=0)
exit_btn.grid(row=5, column=0)
entry.grid(row=1, column=1)
add_btn.grid(row=2, column=1)
label4.grid(row=3, column=1)
label3.grid(row=4, column=1)
listbox.grid(row=5, column=1)

root.mainloop()