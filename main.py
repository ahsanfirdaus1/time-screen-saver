from tkinter import * 
import time 
from typing import Sized

Screen = Tk()

Screen.attributes("-fullscreen", True)
Screen.bind("<F11>", lambda event: Screen.attributes("-fullscreen", not Screen.attributes("-fullscreen")))
Screen.bind("<Escape>", lambda event: Screen.attributes("-fullscreen", False))

Screen.title('Timer by Ahsan')
Screen.geometry('1400x800')
Screen.config(bg="black")

def jalankanWaktu():

    hariSekarang = time.strftime("%A")
    jamSekarang = time.strftime("%H")
    menitSekarang = time.strftime("%M")
    detikSekarang = time.strftime("%S")

    labelWaktu.config(text= hariSekarang.upper() + "\n" + jamSekarang + ":" + menitSekarang + ":" + detikSekarang )
    labelWaktu.after(1000, jalankanWaktu)
    #Update setiap 1 detik sekali 

labelWaktu = Label(Screen, text = "", font= ("Kameron", 60), fg = "#03fc35", bg = "black" )
labelWaktu.pack(pady= 250)

jalankanWaktu()

Screen.mainloop()
