#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x250")

#Create a frame
frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

can = Canvas(frame,bg="white",width=600,height=250)
can.place(x=0,y=0)
#Create a text label
xi=Label(frame,text="Enter the Password", font=('Helvetica',20))
xi.place(x=100,y=100)

def clear_frame():
   for widgets in frame.winfo_children():
      print(widgets)

#Create a button to close the window
Button(frame, text="Clear", font=('Helvetica bold', 10), command=
clear_frame).pack(pady=20)

win.mainloop()
