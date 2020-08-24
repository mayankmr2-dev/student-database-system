import time
from tkinter import *
from tkinter import Toplevel
import random


colors = ['red', 'green', 'yellow', 'pink', 'gold', 'red2']

########### Connect to db button ############


def Connectdb():
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
                          font=('times', 15, 'bold'), relief=RIDGE, bd=3, activebackground="#ccb3b8", activeforegroun="#80ffff")  # you can use bd=3
    SubmitButton.place(x=80, y=200, width=180, height=40)
    dbroot.mainloop()

###################################################################################################################


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
    DataEntryFrame, text='1.   Add Student', width=25,  font=('times', 18, 'italic'), relief=GROOVE, bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
AddButton.pack(side=TOP, expand=True)
SearchButton = Button(
    DataEntryFrame, text='2.   Search Student', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
SearchButton.pack(side=TOP, expand=True)
DeleteButton = Button(
    DataEntryFrame, text='3.   Delete Student', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
DeleteButton.pack(side=TOP, expand=True)
UpdateButton = Button(
    DataEntryFrame, text='4.   Update Student', width=25, font=('times', 18, 'italic'), relief=GROOVE,  bg="#cdd0ae", activebackground="#ccb3b8", activeforegroun="#80ffff", borderwidth=2)
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
root.mainloop()
