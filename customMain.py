from hashlib import new
from tkinter import * 
from typing import Sized 
import time 
import random

myScreen = Tk()

myScreen.attributes("-fullscreen", True)
myScreen.bind("<F11>", lambda event: myScreen.attributes("-fullscreen", not myScreen.attributes("-fullscreen")))
myScreen.bind("<Escape>", lambda event:myScreen.attributes("-fullscreen", False))

def pickTheColour():
    theColours = ["red", "green", "blue", "black", "purple"]
    pickOne = random.choice(theColours)
    return pickOne

def changeTheColour(pickOne):
    myScreen.config(bg= pickOne)
    timeLabel.config(bg = pickOne)

def changeColourPlease():
    newColour = pickTheColour()
    changeTheColour(newColour)

refresh = PhotoImage(file = "C:/_data/_Ahsan/New_Data_3Nov_2020/Belajar Coding/003 - Python/008 - Python Project For Lab TI/001 - Custom Time Screen Saver/refresh.png")

myScreen.title('Time by Ahsan')
myScreen.config(bg = "black")


def thisTime():
    dayToday = time.strftime("%A")
    hourToday = time.strftime("%H")
    minuteToday = time.strftime("%M")
    secondToday = time.strftime("%S")

    timeLabel.config(text = dayToday.upper() + "\n" + hourToday + ":" + minuteToday + ":" + secondToday )
    timeLabel.after(1000, thisTime)

timeLabel = Label(myScreen, text = "", font = ("Kameon", 86), fg = "white", bg = "black")
timeLabel.pack(pady = 150)

changeColorButton = Button(myScreen,bg = "white", height= 1, width = 1, command= changeColourPlease).pack()

thisTime()


myScreen.mainloop()