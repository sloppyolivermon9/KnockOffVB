#Modules
from tkinter import *
from tkinter import messagebox
import sys
#-------------------------------------------------------------------------------

#Variables/System Config
Running_askname = False
InputBox_Result = False
InputBox_Running = False
#-------------------------------------------------------------------------------

#Functions
def QuitProgram():
    global MainWindow
    global inputbox
    MainWindow.quit()
    MainWindow.destroy()
    global InputBox_Result
    if InputBox_Running == True:
        inputbox.quit()
        inputbox.destroy()
    sys.exit()

def InputBox_GetValue():
    global Input
    global InputBox_Running
    global InputBox_Result
    InputBox_Result = Input.get()
    #return str(Input.get())
    inputbox.quit()
    inputbox.destroy()
    InputBox_Running = False

def InputBox(question):
    global inputbox
    global InputBox_Running
    InputBox_Running = True
    inputbox = Tk()
    inputbox.geometry("350x100")
    inputbox.title("InputBox")
    Question = Label(inputbox, text=question)
    Question.place(x=10,y=0)
    global Input
    Input = Entry(inputbox, width=50)
    Input.place(x=10,y=35)
    Confirm = Button(inputbox, text="Enter", command=InputBox_GetValue)
    Confirm.place(x=275,y=60)
    Quit = Button(inputbox, text="Exit Program", command=QuitProgram)
    Quit.place(x=190,y=60)
    inputbox.mainloop()
    global InputBox_Result #Ding Dong My Research Was Wrong
    return InputBox_Result #WHYYYY WHY DOES THIS WORK THIS IS STUPID

def askname():
    global Running_askname
    if Running_askname == False:
        Running_askname = True
        name = InputBox("What is your name?")
        age = InputBox("How old are you?")
        
        ListBox.insert(END, "Your name is: " + name)
        ListBox.insert(END, "You are: " + age + " years old")
        
#-------------------------------------------------------------------------------

#Display
MainWindow = Tk()
MainWindow.geometry("1000x600")
MainWindow.title("InputBox Testing")

title = Label(MainWindow, text="InputBox Testing", font=("Arial",26))
title.pack()

StartButton = Button(MainWindow, text="start", width=25, height=5, command=askname)
StartButton.place(x=800,y=100)

EndButton = Button(MainWindow, text="Quit", width=25, height=5, command=QuitProgram)
EndButton.place(x=800, y=450)

ListBox = Listbox(MainWindow, width=100, height=27)
ListBox.place(x=100, y=100)

MainWindow.mainloop()
#-------------------------------------------------------------------------------
#standard font size for this program is 15 and standard font is Arial

