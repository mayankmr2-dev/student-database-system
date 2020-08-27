# CRUD OPERATION tkinter

from tkinter import *

root = Tk()
root.title('CRUD software')
root.config(bg="#eb3877")
root.iconbitmap('database.ico')
root.geometry('550x450+320+120')


############## Frames & Label #############
LabelName = Label(root, text="CRUD OPERATION", font=(
    'times', 20, 'bold'), fg="#004080", bg="#e4ddfd", relief=SOLID, bd=5)
LabelName.place(x=70, y=8, width=400, height=45)


EntryFrame = Frame(root, bg="#91e199", relief=RIDGE, borderwidth=3)
EntryFrame.place(x=10, y=70, width=250, height=260)

ButtonFrame = Frame(root, bg="#f7baa4", relief=GROOVE, borderwidth=3)
ButtonFrame.place(x=10, y=350, width=250, height=60)

ShowFrame = Frame(root, relief=RIDGE, bd=4)
ShowFrame.place(x=300, y=70, width=220, height=300)


root.mainloop()
