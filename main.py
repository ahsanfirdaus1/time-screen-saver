from tkinter import * 
import time 
from typing import Sized

Screen = Tk()

Screen.attributes("-fullscreen", True)
Screen.bind("<F11>", lambda event: Screen.attributes("-fullscreen", not Screen.attributes("-fullscreen")))
Screen.bind("<Escape>", lambda event: Screen.attributes("-fullscreen", False))

Screen.mainloop()
