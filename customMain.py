from tkinter import * 
from typing import Sized 
import time 
import random 

myScreen = Tk()

myScreen.attributes("-fullscreen", True)
myScreen.bind("<F11>", lambda event: myScreen.attributes("-fullscreen", not myScreen.attributes("-fullscreen")))
myScreen.bind("<Escape>", lambda event:myScreen.attributes("-fullscreen", False))

myScreen.title('Time by Ahsan')
myScreen.config(bg = "black")

if myScreen.bind("<Escape>") == True:
    myScreen.config(bg = "blue")

myScreen.mainloop()