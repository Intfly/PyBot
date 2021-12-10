from tkinter import *

fen = Tk()
fen.geometry("750x500")
fen.title("PyBot")
can = Canvas(fen,bg="white", height=500, width=750)
can.place(x=0,y=0)
linear_gradent_home = PhotoImage(file="images/linear-gradient-home.png")
can.create_image(-40,0,image=linear_gradent_home)
button_home_img = PhotoImage(file="images/button-home.png")
button_home_img_resized = button_home_img.shrink(x=100,y=10)
button_home = Button(can, text = 'tutoriel', image = button_home_img_resized,width= 150,height=30,relief=FLAT,bg="white",highlightbackground="white")
button_home.place(x=460,y=150)
fen.mainloop()