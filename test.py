from tkinter import *

tkWindow = Tk()  
tkWindow.geometry('1000x1000')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def t():
    button.place(x=280,y=365) 
    b=button
    b.place(x=780,y=365)
    b['text'] = 'Submitted'
button = Button(tkWindow,text = 'Submit',command=t) 
t()


tkWindow.mainloop()
