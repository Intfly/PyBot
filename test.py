# Python program to determine which
# button was pressed in tkinter
  
# Import the library tkinter
from tkinter import *
  
# Create a GUI app
app = Tk()
  
# Create a function with one paramter, i.e., of 
# the text you want to show when button is clicked
def which_button(button_press):
    # Printing the text when a button is clicked
    print(button_press)
  
  
# Creating and displaying of button b1
b1 = Button(app, text="Apple",
            command=lambda m="It is an apple": which_button(m))
  
b1.grid(padx=10, pady=10)
  
# Creating and displaying of button b2
b2 = Button(app, text="Banana",
            command=lambda m="It is a banana": which_button(m))
b2.grid(padx=10, pady=10)
  
# Make the infinite loop for displaying the app
app.mainloop()
