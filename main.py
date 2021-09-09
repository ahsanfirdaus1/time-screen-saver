from tkinter import * 
import time 
from typing import Sized

Screen = Tk()

Screen.attributes("-fullscreen", True)
Screen.bind("<F11>", lambda event: Screen.attributes("-fullscreen", not Screen.attributes("-fullscreen")))
Screen.bind("<Escape>", lambda event: Screen.attributes("-fullscreen", False))

labelWaktu = Label(Screen, text = "", font= ("Kameron", 60), fg = "#03fc35", bg = "black" )
labelWaktu.pack(pady= 250)

Screen.mainloop()
