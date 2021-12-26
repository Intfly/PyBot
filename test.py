#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()
def oui():
   x=ent.get()
   print(x)
#Set the geometry of frame
win.geometry("600x250")
def ftn():
   global ent
   ent = Entry(win,bg="#000",fg ='white',relief=FLAT,width=200)
   ent.place(x=100,y=100)
   b=Button(win,command=oui)
   b.place(x=200,y=200)


ftn()
win.mainloop()
