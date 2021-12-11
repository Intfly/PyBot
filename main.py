from tkinter import *
import tkinter.font as font
import webbrowser

fen = Tk()
fen.geometry("750x500")
fen.title("PyBot")

can = Canvas(fen,bg="white", height=500, width=750)
can.place(x=0,y=0)

def tuto_1():
    can.delete(ALL)
    button_home_act_n.destroy()
    button_home_act_t.destroy()
    can.create_text(150,50,fill="black",text="prérequis:",font=Font_desc)
    can.create_text(300,150,fill="black",text="-ouvrez le portail de développeur discord:\n\n\n-connectez-vous",font=Font_desc)
    button_link.place(x=150,y=150)

def nouveau_1():
    can.delete(ALL)
    button_home_act_n.destroy()
    button_home_act_t.destroy()

Font_button = font.Font(family="Abadi MT",size=14,weight="bold")
Font_PyBot = font.Font(family="Gadugi",size=22,weight="bold")
Font_desc = font.Font(family="Arial Baltic",size=14)


linear_gradent_home = PhotoImage(file="nsi-1ere\images\linear-gradient-home.png")
can.create_image(-40,0,image=linear_gradent_home)
text_home_description= can.create_text(70,100,fill="white",text="PyBot",font=Font_PyBot)
text_home_description= can.create_text(160,135,fill="white",text="Créez votre propre bot discord",font=Font_desc)
button_home_img = PhotoImage(file="nsi-1ere\images\-button-home.png")
button_home_img_resized = button_home_img.subsample(2)

button_home_act_t = Button(can,image = button_home_img_resized,width= 180,height=40,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",highlightbackground="white",text = 'tutoriel',compound="center",font=Font_button,command=tuto_1)
button_home_act_t.place(x=460,y=150)
button_home_act_n = Button(can,image = button_home_img_resized,width= 180,height=40,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",highlightbackground="white",text = 'nouveau',compound="center",font=Font_button,command=nouveau_1)
button_home_act_n.place(x=460,y=270)
button_link= Button(can,image = button_home_img_resized,width= 75,height=20,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",highlightbackground="white",text = 'nouveau',compound="center",font=Font_button,command=nouveau_1)
fen.mainloop()