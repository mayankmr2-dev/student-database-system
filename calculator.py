from tkinter import *

root = Tk()
root.title("Calculator")
root.config(bg="#bdd5ac")
root.iconbitmap('cal.ico')
root.geometry('500x500+400+120')  # X * Y + X + Y
root.resizable(False, False)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font=('times', 25, 'bold'))
# padding and internal padding defines size of entry
screen.pack(side=TOP, fill=X, padx=10, pady=10, ipady=5)

################################## Number Frames ###################
numframe = Frame(root, relief=RIDGE, borderwidth=3)
numframe.place(x=15, y=80, width=320, height=400)

b = Button(numframe, text="9", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=0, column=0, padx=(10, 0), pady=5)
b = Button(numframe, text="8", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=0, column=1, pady=5)
b = Button(numframe, text="7", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=0, column=2, padx=(0, 10), pady=5)

b = Button(numframe, text="6", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=1, column=0, padx=(10, 0), pady=5)
b = Button(numframe, text="5", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=1, column=1, pady=5)
b = Button(numframe, text="4", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=1, column=2, padx=(0, 10), pady=5)

b = Button(numframe, text="3", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=2, column=0, padx=(10, 0), pady=5)
b = Button(numframe, text="2", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=2, column=1, pady=5)
b = Button(numframe, text="1", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=2, column=2, padx=(0, 10), pady=5)

b = Button(numframe, text="0", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=3, column=0, padx=(10, 0), pady=5)
b = Button(numframe, text="C", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=3, column=1, pady=5)
b = Button(numframe, text="=", padx=25, pady=12, font=('times', 25, 'bold'))
b.grid(row=3, column=2, padx=(0, 10), pady=5)
################################## Operator Frames #################

opframe = Frame(root, relief=RIDGE, borderwidth=3)
opframe.place(x=365, y=80, width=120, height=400)

p = Button(opframe, text="+", padx=30, pady=18, font=("times", 25, "bold"))
p.pack(side=TOP, fill=X, padx=5, pady=(5, 0))
p = Button(opframe, text="-", padx=30, pady=18, font=("times", 25, "bold"))
p.pack(side=TOP, fill=X, padx=5)
p = Button(opframe, text="/", padx=30, pady=18, font=("times", 25, "bold"))
p.pack(side=TOP, fill=X, padx=5)
p = Button(opframe, text="X", padx=30, pady=18, font=("times", 25, "bold"))
p.pack(side=TOP, fill=X, padx=5, pady=(0, 5))

root.mainloop()
