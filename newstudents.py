# CRUD OPERATION tkinter
import pyodbc
from tkinter import *
from tkinter.ttk import Treeview, Style
from tkinter import messagebox
import os
######### Functions #############

my_server = os.environ['my_server']
my_password = os.environ['my_password']
global conn, cursor


def insert():
    id = idval.get()
    name = nameval.get()
    phone = phoneval.get()

    if (id == "" or name == "" or phone == ""):
        messagebox.showerror("Insert Status", "Please fill all fields !")

    else:
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
                              f"Server={my_server};"
                              "Database=practicemk;"
                              "Uid=mayankmr2;"
                              f"Pwd={my_password};")
        cursor = conn.cursor()
        query = f"insert into Emppractice values(?,?,?)"
        cursor.execute(query, (id, name, phone))
        conn.commit()

        messagebox.showinfo("Successful", "Successful entry !")
        conn.close()
        showall()


def showall():
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
                          f"Server={my_server};"
                          "Database=practicemk;"
                          "Uid=mayankmr2;"
                          f"Pwd={my_password};")
    cursor = conn.cursor()
    cursor.execute('select * from Emppractice')
    datas = cursor.fetchall()
    EmpTable.delete(*EmpTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2]]
        EmpTable.insert('', END, values=vv)


def update():
    id = idval.get()
    name = nameval.get()
    phone = phoneval.get()
    if (id == "" or name == "" or phone == ""):
        messagebox.showerror("Insert Status", "Please fill all fields !")

    else:
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
                              f"Server={my_server};"
                              "Database=practicemk;"
                              "Uid=mayankmr2;"
                              f"Pwd={my_password};")
        cursor = conn.cursor()
        query = f"Update Emppractice set name=?,phone=? where id=?"
        cursor.execute(query, (name, phone, id))
        conn.commit()

        messagebox.showinfo("Updated", "Successful entry !")
        conn.close()
        showall()


def delete():
    id = idval.get()
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
                          f"Server={my_server};"
                          "Database=practicemk;"
                          "Uid=mayankmr2;"
                          f"Pwd={my_password};")
    cursor = conn.cursor()
    query = f"Delete from Emppractice where id=?"
    cursor.execute(query, (id))
    conn.commit()

    messagebox.showinfo("Deleted", "Successfully Deleted !")
    conn.close()
    showall()


def get():
    id = idval.get()
    name = nameval.get()
    phone = phoneval.get()

    if (id == ""):
        messagebox.showerror("Missing", "Please enter ID !")
    else:
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
                              f"Server={my_server};"
                              "Database=practicemk;"
                              "Uid=mayankmr2;"
                              f"Pwd={my_password};")
        cursor = conn.cursor()
        query = f"Select * from Emppractice where id=?"
        cursor.execute(query, (id))
        rows = cursor.fetchall()

        for row in rows:
            nameval.set(row[1])
            phoneval.set(row[2])
        conn.close()


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
ButtonFrame.place(x=10, y=350, width=360, height=60)

ShowFrame = Frame(root, relief=RIDGE, bd=4)
ShowFrame.place(x=300, y=70, width=220, height=260)

############# Treeview #####################


############# Entry Frame widgets ###########
idval = StringVar()
nameval = StringVar()
phoneval = StringVar()


e_id = Label(EntryFrame, text="Emp_ID", font=('times', 12, 'bold'))
e_id.place(x=15, y=12)

e_id = Entry(EntryFrame, text="Emp_ID", width=25, textvariable=idval)
e_id.place(x=15, y=52)

e_name = Label(EntryFrame, text="Emp_Name", font=('times', 12, 'bold'))
e_name.place(x=15, y=92)

e_name = Entry(EntryFrame, text="Emp_ID", width=25, textvariable=nameval)
e_name.place(x=15, y=132)

e_phone = Label(EntryFrame, text="Emp_Phone", font=('times', 12, 'bold'))
e_phone.place(x=15, y=172)

e_phone = Entry(EntryFrame, text="Emp_ID", width=25, textvariable=phoneval)
e_phone.place(x=15, y=212)

########### ShowFrame ############

style = Style()
# ["aqua", "step", "clam", "alt", "default", "classic"]
style.theme_use("classic")
style.configure('Treeview.Heading', font=(
    'times', 10, 'bold'), foreground='black')
style.configure('Treeview', font=('times', 7, 'bold'),
                background="yellow", foreground='black')
scroll_x = Scrollbar(ShowFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowFrame, orient=VERTICAL)
EmpTable = Treeview(ShowFrame, columns=('ID', 'Name', 'Phone'),
                    yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=EmpTable.xview)
scroll_y.config(command=EmpTable.yview)
EmpTable.heading('ID', text='ID')
EmpTable.heading('Name', text='Name')
EmpTable.heading('Phone', text='Phone')

EmpTable['show'] = 'headings'

EmpTable.column('ID', width=60)
EmpTable.column('Name', width=120)
EmpTable.column('Phone', width=120)

EmpTable.pack(fill=BOTH, expand=1)

showall()
############ focus #################################
############# ButtonFrame buttons ##################
Addbtn = Button(ButtonFrame, text="ADD", font=(
    "times", 12, "bold"), relief=GROOVE, command=insert)
Addbtn.place(x=15, y=10)
Updatebtn = Button(ButtonFrame, text="UPDATE", font=(
    "times", 12, "bold"), relief=GROOVE, command=update)
Updatebtn.place(x=75, y=10)
Deletebtn = Button(ButtonFrame, text="DELETE", font=(
    "times", 12, "bold"), relief=GROOVE, command=delete)
Deletebtn.place(x=165, y=10)
Getbtn = Button(ButtonFrame, text="GET", font=(
    "times", 12, "bold"), relief=GROOVE, command=get)
Getbtn.place(x=255, y=10)


root.mainloop()
