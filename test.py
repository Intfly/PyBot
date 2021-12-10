#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of Tkinter Frame
win.geometry("700x350")

#Define a function for exit
def exit_program():
   win.destroy()


#Add a canvas widget
canvas = Canvas(win, width= 350)

#Add a Label widget in the Canvas
label = Label(canvas, text= "Click the Button to Exit", font= ('Helvetica 17 bold'))
label.pack(pady= 30)

#Create a button in canvas widget
ttk.Button(canvas, text= "Exit", command= exit_program).pack()
canvas.pack()

win.mainloop()