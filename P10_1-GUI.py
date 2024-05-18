#import tkinter as tk
import P10KimlikOkuma
from tkinter import *
_id, _surname = P10KimlikOkuma.IdSurnameConvert()
master = Tk()

canvas = Canvas(master, height=550, width = 850)
canvas.pack()

mainFrame = Frame(master, bg= "#add8e6" )
mainFrame.place(relx=0.1, rely=0.1, relwidth=0.75, relheight= 0.75)

if P10KimlikOkuma.tc_isim_kontrol(_id, _surname):
    mevcutEtiket = Label(mainFrame, bg= "#add8ea", text="TC ve Soyisim veri \n tabanı içinde bulunuyor.", font="Verdana 22 bold")
    mevcutEtiket.pack(padx=10,pady=30)
else:
    mevcutEtiket = Label(mainFrame, bg= "#add8ea", text="TC ve Soyisim veri \n tabanı içinde bulunmamaktadır.", font="Verdana 22 bold")
    mevcutEtiket.pack(padx=10,pady=30)
    
idEtiket = Label(mainFrame, bg= "#add8ea", text=f"TC = {_id} \n Soyisim = {_surname}", font="Verdana 22 bold")
idEtiket.pack(padx=10,pady=30)

#naMevcutEtiket = Label(mainFrame, bg= "#add8ea", text="TC ve Soyisim veri tabanı içinde bulunmuyor.")

master.mainloop()