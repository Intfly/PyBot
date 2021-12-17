#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x250")

#Create a frame
frame = Frame(win)
frame.pack(side="top", expand=True, fill="both")

#Create a text label
Label(frame,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

#Create a button to close the window
Button(frame, text="Clear", font=('Helvetica bold', 10), command=
clear_frame).pack(pady=20)

win.mainloop()