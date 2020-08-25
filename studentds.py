import time
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from tkinter import Toplevel
from tkinter import messagebox
import random
import pyodbc


colors = ['red', 'green', 'yellow', 'pink', 'gold', 'red2']
# Fonts = ('times',30,'italic/bold) Helvetica,chiller


########### Connect to db button ############


def Connectdb():
    def connecteddb():
        global conn, cursor
        host = Hostval.get()
        user = Userval.get()
        password = Passwordval.get()
        try:
            conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"  # For Connection
                                  f"Server={host};"
                                  "Database=practicemk;"
                                  f"Uid={user};"
                                  f"Pwd={password};")
            cursor = conn.cursor()
            query1 = "create table studentdata(id int not null primary key,name varchar(20),mobile varchar(12),email varchar(30),address varchar(40),gender varchar(10),dob varchar(20),date varchar(30),time varchar(30))"
            cursor.execute(query1)
            cursor.commit()
            messagebox.showinfo(
                'Information', 'Successful')
            dbroot.destroy()

        except:
            messagebox.showerror(
                'Notifications', 'Input data is Invalid !\nTry again')
            return

    dbroot = Toplevel()
    dbroot.grab_set()
    # will not be able to use the background main application and focus stays on current window
    dbroot.geometry("470x250+800+230")
    dbroot.iconbitmap('database.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='#aa73e8')

    HostLabel = Label(dbroot, bg="#0bb5a4", text="Host    :",
                      font=('times', 20, 'bold'), relief=RIDGE, bd=3)  # you can use bd=3
    HostLabel.place(x=8, y=10, width=180, height=40)
    UserLabel = Label(dbroot, bg="#0bb5a4", text="User    :",
                      font=('times', 20, 'bold'), relief=RIDGE, bd=3)  # you can use bd=3
    UserLabel.place(x=8, y=75, width=180, height=40)
    PasswordLabel = Label(dbroot, bg="#0bb5a4", text="Password  :",
                          font=('times', 20, 'bold'), relief=RIDGE, bd=3)  # you can use bd=3
    PasswordLabel.place(x=8, y=140, width=180, height=40)

    Hostval = StringVar()    # Hostval.get('Hello') - This will print hello in the Entry
    Userval = StringVar()
    Passwordval = StringVar()

    HostText = Entry(dbroot, relief=RIDGE, bd=3,
                     textvariable=Hostval)  # you can use bd=3
    HostText.place(x=240, y=10, width=180, height=40)
    UserText = Entry(
        dbroot,  relief=RIDGE, bd=3, textvariable=Userval)  # you can use bd=3
    UserText.place(x=240, y=75, width=180, height=40)
    PasswordText = Entry(
        dbroot, relief=RIDGE, bd=3, textvariable=Passwordval)  # you can use bd=3
    PasswordText.place(x=240, y=140, width=180, height=40)
    SubmitButton = Button(dbroot, bg="#cdd0ae", text="SUBMIT",
                          font=('times', 15, 'bold'), relief=RIDGE, bd=3, activebackground="#ccb3b8",
                          activeforegroun="#80ffff", command=connecteddb)  # you can use bd=3
    SubmitButton.place(x=80, y=200, width=180, height=40)
    dbroot.mainloop()

############## Add Student ###################


def AddStudent():
    def submitadd():
        # nameentry.get() Student Added Successfully ! Mayan
        print("Student Added Successfully ! ")
    addroot = Toplevel(master=DataEntryFrame)
    addroot.title('Add Student')
    addroot.grab_set()
    addroot.geometry("450x520+220+120")
    addroot.iconbitmap('student.ico')
    addroot.resizable(False, False)
    addroot.config(bg='#aa73e8')

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addrval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    idlabel = Label(addroot, text="Enter id  :", font=('times', 15, 'bold'),
                    width=15, relief=RIDGE, bd=3)
    idlabel.grid(row=0, column=0, padx=10, pady=15)

    identry = Entry(addroot, relief=RIDGE, width=20, font=(
        'times', 15), bd=3, textvariable=idval)
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(addroot, text="Enter name  :", font=('times', 15, 'bold'),
                      width=15, relief=RIDGE, bd=3)
    namelabel.grid(row=1, column=0, padx=10, pady=15)

    nameentry = Entry(addroot, relief=RIDGE, width=20,
                      font=('times', 15), bd=3, textvariable=nameval)
    nameentry.grid(row=1, column=1, padx=10, pady=15)
    mobilelabel = Label(addroot, text="Enter mobile  :", font=('times', 15, 'bold'),
                        width=15, relief=RIDGE, bd=3)
    mobilelabel.grid(row=2, column=0, padx=10, pady=15)

    mobileentry = Entry(addroot, relief=RIDGE, width=20,
                        font=('times', 15), bd=3, textvariable=mobileval)
    mobileentry.grid(row=2, column=1, padx=10, pady=15)
    emaillabel = Label(addroot, text="Enter email  :", font=('times', 15, 'bold'),
                       width=15, relief=RIDGE, bd=3)
    emaillabel.grid(row=3, column=0, padx=10, pady=15)

    emailentry = Entry(addroot, relief=RIDGE, width=20,
                       font=('times', 15), bd=3, textvariable=emailval)
    emailentry.grid(row=3, column=1, padx=10, pady=15)
    addresslabel = Label(addroot, text="Enter address  :", font=('times', 15, 'bold'),
                         width=15, relief=RIDGE, bd=3)
    addresslabel.grid(row=4, column=0, padx=10, pady=15)

    addressentry = Entry(addroot, relief=RIDGE, width=20,
                         font=('times', 15), bd=3, textvariable=addrval)
    addressentry.grid(row=4, column=1, padx=10, pady=15)
    genderlabel = Label(addroot, text="Enter Gender  :", font=('times', 15, 'bold'),
                        width=15, relief=RIDGE, bd=3)
    genderlabel.grid(row=5, column=0, padx=10, pady=15)

    genderentry = Entry(addroot, relief=RIDGE, width=20,
                        font=('times', 15), bd=3, textvariable=genderval)
    genderentry.grid(row=5, column=1, padx=10, pady=15)
    doblabel = Label(addroot, text="Enter D.O.B.  :", font=('times', 15, 'bold'),
                     width=15, relief=RIDGE, bd=3)
    doblabel.grid(row=6, column=0, padx=10, pady=15)

    dobentry = Entry(addroot, relief=RIDGE, width=20,
                     font=('times', 15), bd=3, textvariable=dobval)
    dobentry.grid(row=6, column=1, padx=10, pady=15)
    Submitbtn = Button(addroot, text="SUBMIT", font=('times', 15, 'bold'), bg="#8080ff",
                       relief=RIDGE, bd=4, activebackground="#ccb3b8", activeforeground="#80ffff", command=submitadd)
    Submitbtn.grid(row=7, columnspan=2, padx=20, pady=20)

    addroot.mainloop()

############ Search Student ################


def SearchStudent():
    def search():
        print("Searching ....")

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.title('Search Student')
    searchroot.grab_set()
    searchroot.geometry("450x600+220+120")
    searchroot.iconbitmap('student.ico')
    searchroot.resizable(False, False)
    searchroot.config(bg='#94a857')

    idval3 = StringVar()
    nameval3 = StringVar()
    mobileval3 = StringVar()
    emailval3 = StringVar()
    addrval3 = StringVar()
    genderval3 = StringVar()
    dobval3 = StringVar()
    dateval3 = StringVar()

    idlabel = Label(searchroot, text="Enter id  :", font=('times', 15, 'bold'),
                    width=15, relief=RIDGE, bd=3)
    idlabel.grid(row=0, column=0, padx=10, pady=15)

    identry = Entry(searchroot, relief=RIDGE, width=20, font=(
        'times', 15), bd=3, textvariable=idval3)
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(searchroot, text="Enter name  :", font=('times', 15, 'bold'),
                      width=15, relief=RIDGE, bd=3)
    namelabel.grid(row=1, column=0, padx=10, pady=15)

    nameentry = Entry(searchroot, relief=RIDGE, width=20,
                      font=('times', 15), bd=3, textvariable=nameval3)
    nameentry.grid(row=1, column=1, padx=10, pady=15)
    mobilelabel = Label(searchroot, text="Enter mobile  :", font=('times', 15, 'bold'),
                        width=15, relief=RIDGE, bd=3)
    mobilelabel.grid(row=2, column=0, padx=10, pady=15)

    mobileentry = Entry(searchroot, relief=RIDGE, width=20,
                        font=('times', 15), bd=3, textvariable=mobileval3)
    mobileentry.grid(row=2, column=1, padx=10, pady=15)
    emaillabel = Label(searchroot, text="Enter email  :", font=('times', 15, 'bold'),
                       width=15, relief=RIDGE, bd=3)
    emaillabel.grid(row=3, column=0, padx=10, pady=15)

    emailentry = Entry(searchroot, relief=RIDGE, width=20,
                       font=('times', 15), bd=3, textvariable=emailval3)
    emailentry.grid(row=3, column=1, padx=10, pady=15)
    addresslabel = Label(searchroot, text="Enter address  :", font=('times', 15, 'bold'),
                         width=15, relief=RIDGE, bd=3)
    addresslabel.grid(row=4, column=0, padx=10, pady=15)

    addressentry = Entry(searchroot, relief=RIDGE, width=20,
                         font=('times', 15), bd=3, textvariable=addrval3)
    addressentry.grid(row=4, column=1, padx=10, pady=15)
    genderlabel = Label(searchroot, text="Enter Gender  :", font=('times', 15, 'bold'),
                        width=15, relief=RIDGE, bd=3)
    genderlabel.grid(row=5, column=0, padx=10, pady=15)

    genderentry = Entry(searchroot, relief=RIDGE, width=20,
                        font=('times', 15), bd=3, textvariable=genderval3)
    genderentry.grid(row=5, column=1, padx=10, pady=15)
    doblabel = Label(searchroot, text="Enter D.O.B.  :", font=('times', 15, 'bold'),
                     width=15, relief=RIDGE, bd=3)
    doblabel.grid(row=6, column=0, padx=10, pady=15)

    dobentry = Entry(searchroot, relief=RIDGE, width=20,
                     font=('times', 15), bd=3, textvariable=dobval3)
    dobentry.grid(row=6, column=1, padx=10, pady=15)
    datelabel = Label(searchroot, text="Enter Date  :", font=('times', 15, 'bold'),
                      width=15, relief=RIDGE, bd=3)
    datelabel.grid(row=7, column=0, padx=10, pady=15)

    dateentry = Entry(searchroot, relief=RIDGE, width=20,
                      font=('times', 15), bd=3, textvariable=dateval3)
    dateentry.grid(row=7, column=1, padx=10, pady=15)

    Submitbtn = Button(searchroot, text="SUBMIT", font=('times', 15, 'bold'), bg="#8080ff",
                       relief=RIDGE, bd=4, activebackground="#ccb3b8", activeforeground="#80ffff", command=search)
    Submitbtn.grid(row=9, columnspan=2, padx=20, pady=20)

    searchroot.mainloop()


def UpdateStudent():
    def submitupdate():
        # nameentry.get() Student Added Successfully ! Mayan
        print("Student updated Successfully ! ")
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.title('Update Student')
    updateroot.grab_set()
    updateroot.geometry("450x650+220+120")
    updateroot.iconbitmap('student.ico')
    updateroot.resizable(False, False)
    updateroot.config(bg='#54e1ed')

    idval2 = StringVar()
    nameval2 = StringVar()
    mobileval2 = StringVar()
    emailval2 = StringVar()
    addrval2 = StringVar()
    genderval2 = StringVar()
    dobval2 = StringVar()
    dateval2 = StringVar()
    timeval2 = StringVar()

    idlabel = Label(updateroot, text="Enter id  :", font=('times', 15, 'bold'),
                    width=15, relief=RIDGE, bd=3)
    idlabel.grid(row=0, column=0, padx=10, pady=15)

    identry = Entry(updateroot, relief=RIDGE, width=20, font=(
        'times', 15), bd=3, textvariable=idval2)
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(updateroot, text="Enter name  :", font=('times', 15, 'bold'),
                      width=15, relief=RIDGE, bd=3)
    namelabel.grid(row=1, column=0, padx=10, pady=15)

    nameentry = Entry(updateroot, relief=RIDGE, width=20,
                      font=('times', 15), bd=3, textvariable=nameval2)
    nameentry.grid(row=1, column=1, padx=10, pady=15)
    mobilelabel = Label(updateroot, text="Enter mobile  :", font=('times', 15, 'bold'),
                        width=15, relief=RIDGE, bd=3)
    mobilelabel.grid(row=2, column=0, padx=10, pady=15)

    mobileentry = Entry(updateroot, relief=RIDGE, width=20,
                        font=('times', 15), bd=3, textvariable=mobileval2)
    mobileentry.grid(row=2, column=1, padx=10, pady=15)
    emaillabel = Label(updateroot, text="Enter email  :", font=('times', 15, 'bold'),
                       width=15, relief=RIDGE, bd=3)
    emaillabel.grid(row=3, column=0, padx=10, pady=15)

    emailentry = Entry(updateroot, relief=RIDGE, width=20,
                       font=('times', 15), bd=3, textvariable=emailval2)
    emailentry.grid(row=3, column=1, padx=10, pady=15)
    addresslabel = Label(updateroot, text="Enter address  :", font=('times', 15, 'bold'),
                         width=15, relief=RIDGE, bd=3)
    addresslabel.grid(row=4, column=0, padx=10, pady=15)

    addressentry = Entry(updateroot, relief=RIDGE, width=20,
                         font=('times', 15), bd=3, textvariable=addrval2)
    addressentry.grid(row=4, column=1, padx=10, pady=15)
    genderlabel = Label(updateroot, text="Enter Gender  :", font=('times', 15, 'bold'),
                        width=15, relief=RIDGE, bd=3)
    genderlabel.grid(row=5, column=0, padx=10, pady=15)

    genderentry = Entry(updateroot, relief=RIDGE, width=20,
                        font=('times', 15), bd=3, textvariable=genderval2)
    genderentry.grid(row=5, column=1, padx=10, pady=15)
    doblabel = Label(updateroot, text="Enter D.O.B.  :", font=('times', 15, 'bold'),
                     width=15, relief=RIDGE, bd=3)
    doblabel.grid(row=6, column=0, padx=10, pady=15)

    dobentry = Entry(updateroot, relief=RIDGE, width=20,
                     font=('times', 15), bd=3, textvariable=dobval2)
    dobentry.grid(row=6, column=1, padx=10, pady=15)
    datelabel = Label(updateroot, text="Enter Date  :", font=('times', 15, 'bold'),
                      width=15, relief=RIDGE, bd=3)
    datelabel.grid(row=7, column=0, padx=10, pady=15)

    dateentry = Entry(updateroot, relief=RIDGE, width=20,
                      font=('times', 15), bd=3, textvariable=dateval2)
    dateentry.grid(row=7, column=1, padx=10, pady=15)
    timelabel = Label(updateroot, text="Enter Time  :", font=('times', 15, 'bold'),
                      width=15, relief=RIDGE, bd=3)
    timelabel.grid(row=8, column=0, padx=10, pady=15)

    timeentry = Entry(updateroot, relief=RIDGE, width=20,
                      font=('times', 15), bd=3, textvariable=timeval2)
    timeentry.grid(row=8, column=1, padx=10, pady=15)
    Submitbtn = Button(updateroot, text="SUBMIT", font=('times', 15, 'bold'), bg="#8080ff",
                       relief=RIDGE, bd=4, activebackground="#ccb3b8", activeforeground="#80ffff", command=submitupdate)
    Submitbtn.grid(row=9, columnspan=2, padx=20, pady=20)

    updateroot.mainloop()


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)


def IntroLabelTick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    TimeLabel.config(text="Date: "+date_string+"\n"+"Time: "+time_string)
    TimeLabel.after(200, tick)


################ Main Root App Window ###########################
root = Tk()
root.title('Student Management System')
root.config(bg='#91e199')
# width x height + x position of screen + y position of screen
root.geometry('1174x700+200+50')
root.iconbitmap('student.ico')
root.resizable(False, False)
# TCGIR

############## Frames #################

DataEntryFrame = Frame(root, bg="#ff8000", relief=GROOVE,
                       borderwidth=5)  # GROOVE,SOLID,RIDGE
DataEntryFrame.place(x=10, y=90, width=500, height=600)


ShowDataFrame = Frame(root, bg="#ff8000", relief=GROOVE,
                      borderwidth=5)  # GROOVE,SOLID,RIDGE
ShowDataFrame.place(x=620, y=90, width=550, height=600)

############## Slider Label #################
ss = 'Student Management System'
count = 0
text = ''

SliderLabel = Label(root, text=ss, font=('chiller', 38, 'italic bold'), bg="#2bbbd5", relief=RIDGE,
                    borderwidth=3)  # GROOVE,SOLID,RIDGE
SliderLabel.place(x=335, y=0, width=450, height=70)
IntroLabelTick()
IntroLabelColorTick()
############## Time Label #################
TimeLabel = Label(root, text='time', font=('times', 18, 'bold'), bg="#2bbbd5", relief=RIDGE,
                  borderwidth=3)  # GROOVE,SOLID,RIDGE
TimeLabel.place(x=0, y=0, width=200, height=70)
tick()
############## DataEntryFrame ##############

WelcomeLabel = Label(
    DataEntryFrame, text='-------------- WELCOME ---------------', font=('times', 25, 'bold'), relief=GROOVE, bg="#ff8000", borderwidth=2)
WelcomeLabel.pack(side=TOP, expand=True)
AddButton = Button(
    DataEntryFrame, text='1.   Add Student', width=25,  font=('times', 18, 'italic'), relief=GROOVE, bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2, command=AddStudent)
AddButton.pack(side=TOP, expand=True)
SearchButton = Button(
    DataEntryFrame, text='2.   Search Student', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2, command=SearchStudent)
SearchButton.pack(side=TOP, expand=True)
DeleteButton = Button(
    DataEntryFrame, text='3.   Delete Student', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
DeleteButton.pack(side=TOP, expand=True)
UpdateButton = Button(
    DataEntryFrame, text='4.   Update Student', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2, command=UpdateStudent)
UpdateButton.pack(side=TOP, expand=True)
ShowallButton = Button(
    DataEntryFrame, text='5.   Show All', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
ShowallButton.pack(side=TOP, expand=True)
ExportButton = Button(
    DataEntryFrame, text='6.    Export', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
ExportButton.pack(side=TOP, expand=True)
ExitButton = Button(
    DataEntryFrame, text='7.   Exit', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2, command=root.destroy)
ExitButton.pack(side=TOP, expand=True)

############## Connection Button ###########
ConnectionButton = Button(root, text='Connect to Database', font=('times', 15, 'bold'), bg="#008080", relief=RIDGE, activebackground="#ccb3b8", activeforegroun="#80ffff",
                          borderwidth=3, command=Connectdb)  # GROOVE,SOLID,RIDGE
ConnectionButton.place(x=900, y=5, width=200, height=35)

############## ShowDataFrame ###############
style = Style()
style.theme_use("clam")
style.configure('Treeview.Heading', font=(
    'chiller', 20, 'bold'), foreground='black')
style.configure('Treeview', font=(
    'chiller', 18, 'bold'), background="yellow", foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
StudentTable = Treeview(ShowDataFrame, columns=('ID', 'Name', 'Mobile No.',
                                                'Email ID', 'Address', 'Gender', 'D.O.B.', 'Added Date', 'Added Time'), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
# StudentTable.tag_configure("odd", background="yellow")
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=StudentTable.xview)
scroll_y.config(command=StudentTable.yview)
StudentTable.heading('ID', text='ID')
StudentTable.heading('Name', text='Name')
StudentTable.heading('Mobile No.', text='Mobile No.')
StudentTable.heading('Email ID', text='Email ID')
StudentTable.heading('Address', text='Address')
StudentTable.heading('Gender', text='Gender')
StudentTable.heading('D.O.B.', text='D.O.B.')
StudentTable.heading('Added Date', text='Added Date')
StudentTable.heading('Added Time', text='Added Time')

StudentTable['show'] = 'headings'

StudentTable.column('ID', width=60)
StudentTable.column('Name', width=200)
StudentTable.column('Mobile No.', width=200)
StudentTable.column('Email ID', width=200)
StudentTable.column('Address', width=300)
StudentTable.column('Gender', width=80)
StudentTable.column('D.O.B.', width=150)
StudentTable.column('Added Date', width=150)
StudentTable.column('Added Time', width=150)


StudentTable.pack(fill=BOTH, expand=1)

root.mainloop()
