#_*_ coding:cp1254 _*_
from tkinter import *
pencere = Tk()
def tusabas(event):
    print ("basildi",repr(event.char))
def tiklanma(event):
    frame.focus_set()
    print("Mouse Tıklandı",event.x,event.y)
frame = Frame(pencere,width=100,height=100)
frame.bind("<Key>",tusabas)
frame.bind("<Button-1>",tiklanma)
frame.grid(row=0,column=0)

pencere.mainloop()
