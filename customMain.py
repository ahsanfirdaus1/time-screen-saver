from tkinter import * 
from typing import Sized 
import time 
import random 

myScreen = Tk()

myScreen.attributes("-fullscreen", True)
myScreen.bind("<F11>", lambda event: myScreen.attributes("-fullscreen", not myScreen.attributes("-fullscreen")))
myScreen.bind("<Escape>", lambda event:myScreen.attributes("-fullscreen", False))

myColor = ("red","green","blue","white")
thisColor = random.choices(myColor)

myScreen.bind("<Enter>", lambda event: myScreen.config(bg = thisColor))

myScreen.title('Time by Ahsan')
myScreen.config(bg = thisColor)


def thisTime():
    dayToday = time.strftime("%A")
    hourToday = time.strftime("%H")
    minuteToday = time.strftime("%M")
    secondToday = time.strftime("%S")

    timeLabel.config(text = dayToday.upper() + "\n\n" + hourToday + ":" + minuteToday + ":" + secondToday)
    timeLabel.after(1000, thisTime)

timeLabel = Label(myScreen, text = "", fg = thisColor , bg = "black")

thisTime()

myScreen.mainloop()