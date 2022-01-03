from abc import abstractproperty
from tkinter import *
import tkinter.font as font
import webbrowser


fen = Tk()
fen.geometry("750x500")
fen.title("PyBot")


frame_p = Frame(fen)#création d'un frame
frame_p.pack(expand=True, fill="both")#positionnement du canvas,s'étend et remplis l'axe x et y 


can = Canvas(frame_p,bg="white", height=500, width=750)
can.place(x=-2,y=-2)


#variables utiles dans le code
olhelper = 0
guillemets='"'
vect_s2=[]


def supp_a():
    for widgets in frame_p.winfo_children():#parcourt les enfants de la frame "frame_p" et les supprimes tous sauf le canvas
        if widgets.winfo_class() != 'Canvas':
            widgets.destroy()

def menu_home():
    global home_hlp  
    supp_a()
    can.delete(ALL)
    button_home_act_t = Button(frame_p,image = button_home_img_resized,width= 180,height=40,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",text = 'tutoriel',compound="center",font=Font_button,command=tuto_1)
    button_home_act_n = Button(frame_p,image = button_home_img_resized,width= 180,height=40,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",text = 'nouveau',compound="center",font=Font_button,command=nouveau_1)
    button_home_act_n.place(x=460,y=270)
    button_home_act_t.place(x=460,y=150)
    can.create_image(-40,0,image=linear_gradent_home)
    can.create_text(70,100,fill="white",text="PyBot",font=Font_PyBot)
    can.create_text(160,135,fill="white",text="Créez votre propre bot discord",font=Font_desc)
    home_hlp = 1
        
def ftn_commande(cmd):
    global vect_s
    global c1_v
    global c2_v
    global act_nm  
    global ent_fx
    global nb_fois_move
    global cha1
    global cha2
    global nb_fois_deco   
    global message_message
    global message_on_join
    vect_s={}
    vect_s[nom_ftn]=cmd
    #permet de modifier l'UI en fontion de la valeur de cmd(et donc du bouton sur lequel l'utilisateur a cliqué) afin de lui permettre d'insérer des paramètres si nécessaires
    if cmd == 0:
        can.delete(ALL)
        supp_a()  
        can.create_image(0,0, image = linear_gradient_2)
        button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
        button_retour_home.place(x=25,y=450)
        can.create_image(375,215,image = ent2)
        can.create_text(295,170,fill="grey",text="nombre de fois",font=Font_desc)
        ent_fx = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
        ent_fx.place(x=200,y=185,width=350,height=50)
        button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=recupfois_ping)
        button_next.place(x=600,y=450)
    elif cmd == 1:
            can.delete(ALL)
            supp_a()
            can.create_image(0,0, image= linear_gradient_2)
            can.create_image(378,235,image=ent)
            can.create_text(290,110,fill="grey",text="ID du Channel 1",font=Font_desc)
            cha1 = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
            cha1.place(x=225,y=120,width=300,height=50)
            can.create_text(290,200,fill="grey",text="ID du Channel 2",font=Font_desc)
            cha2 = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
            cha2.place(x=225,y=210,width=300,height=50)
            can.create_text(290,290,fill="grey",text="nombre de fois",font=Font_desc)
            nb_fois_move = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_titre,fg="#686868")
            nb_fois_move.place(x=225,y=300,width=300,height=50)
            button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
            button_retour_home.place(x=25,y=450) 
            button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=recupfois_move)
            button_next.place(x=600,y=450)
    elif cmd == 4:
        can.delete(ALL)
        supp_a() 
        can.create_image(0,0, image = linear_gradient_2)
        button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
        button_retour_home.place(x=25,y=450)
        can.create_image(375,215,image = ent2)
        can.create_text(320,170,fill="grey",text="nombre de fois (1 fois toutes les 1.5s) ",font=Font_desc)
        nb_fois_deco = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
        nb_fois_deco.place(x=200,y=185,width=350,height=50)
        button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=recupfois_deco)
        button_next.place(x=600,y=450)         
    elif cmd == 5:
        can.delete(ALL)
        supp_a()
        def change():
            if c1_v.get()==1:
                str_var.set("joue à:")
            if c2_v.get()==1:
                str_var.set("écoute:")
            if c1_v.get()==0 and c2_v.get()==0:
                str_var.set("")
        can.create_image(0,0, image = linear_gradient_2)
        button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
        button_retour_home.place(x=25,y=450)
        can.create_image(378,235,image=ent)
        can.create_text(375,120,fill="grey",text="séléctionnez un bouton",font=Font_desc)
        str_var = StringVar(frame_p,"")
        act_lbl=Label(frame_p,textvariable=str_var,fg="grey",font=Font_desc,bg ="white")
        act_lbl.place(x=200,y=240)
        act_nm = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
        act_nm.place(x=200,y=280,width=350,height=50)
        button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=recup_act)
        button_next.place(x=600,y=450) 
        c1_v = IntVar()
        c2_v = IntVar()
        c1 = Checkbutton(frame_p, text="Joue à:",variable=c1_v, onvalue=1, offvalue=0,bg="white",activebackground="white",font=Font_desc,fg="#686868",activeforeground="#686868",command=change)
        c1.place(x=200,y=150)
        c2 = Checkbutton(frame_p, text="écoute:",variable=c2_v, onvalue=1, offvalue=0,bg="white",activebackground="white",font=Font_desc,fg="#686868",activeforeground="#686868",command=change)
        c2.place(x=400,y=150)
    elif cmd == 6:
        can.delete(ALL)
        supp_a()  
        can.create_image(0,0, image = linear_gradient_2)
        button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
        button_retour_home.place(x=25,y=450)
        can.create_image(375,215,image = ent2)
        can.create_text(295,170,fill="grey",text="message à répondre",font=Font_desc)
        message_message = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
        message_message.place(x=200,y=185,width=350,height=50)
        button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=recup_message)
        button_next.place(x=600,y=450)
    elif cmd == 7:
        can.delete(ALL)
        supp_a()  
        can.create_image(0,0, image = linear_gradient_2)
        button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
        button_retour_home.place(x=25,y=450)
        can.create_image(375,215,image = ent2)
        can.create_text(295,170,fill="grey",text="message à envoyer(en mp)",font=Font_desc)
        message_on_join = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
        message_on_join.place(x=200,y=185,width=350,height=50)
        button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=recup_message_on_join)
        button_next.place(x=600,y=450)
    else:
        interm()#exécute la fonction suivante si cmd(ayant pour valeur i, cf nouveau_3()) correspond à une fonction ne pouvant pas être modifiée par l'utilisateur

#les fonctions sont des fonctions intermédiaires permettant de de récupérer les variables des entrées(permettant de personnaliser les fonctions). Une fonction lambda ajoutant à un tableau la valeur de cmd et ses paramètres éventuels aurait pu marcher et aurait été plus concis mais moins lisible
act_hlp=0
def recup_act():
    global act
    global act_hlp
    act=act_nm.get()
    act_hlp = 1
    interm()#exécute la fonction suivante une fois la valeur récupérée

def recupfois_ping():
    global fois_ping
    fois_ping=ent_fx.get()
    interm()

def recupfois_move():
    global fois_move
    global chan1
    global chan2
    fois_move=int(nb_fois_move.get())//2
    chan1 = cha1.get()
    chan2= cha2.get()
    interm()

def recupfois_deco():
    global fois_deco
    fois_deco = nb_fois_deco.get()
    interm()

def recup_message():
    global message_ftn
    message_ftn= message_message.get()
    interm()

def recup_message_on_join():
    global message_join
    message_join = message_on_join.get()
    interm()

#premier menu en cliquant sur "tutoriel" 
def tuto_1():
    global olhelper
    olhelper = 1
    can.delete(ALL)
    supp_a()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="prérequis",font=Font_titre_gros)
    can.create_text(300,165,fill="white",text="-ouvrez le portail de développeur discord:\n\n\n-connectez-vous",font=Font_desc)
    button_link= Button(frame_p,image = button_open_link,width= 150,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f60bf",text = 'cliquez ici',compound="center",font=Font_button,command=open_link)
    button_link.place(x=150,y=150)
    button_next = Button(frame_p,image = button_next_img_resized,width= 150,height=25,relief=FLAT,bg="#7159b5",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=tuto_2)
    button_next.place(x=575,y=450)
    can.create_image(250,340, image=DDPconnexion_resized)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f62c3",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)  

def tuto_2():

    can.delete(ALL)
    supp_a()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="prérequis",font=Font_titre_gros)
    can.create_text(350,215,fill="white",text="-créez une nouvelle application grâce au bouton en haut à droite",font=Font_desc)
    can.create_image(170,260, image=new_app)
    can.create_text(170,310,fill="white",text="vous y trouverez",font=Font_desc)
    can.create_text(323,310,fill="#ff7583",text="l'ID de l'application",font=Font_desc)
    can.create_text(493,310,fill="white",text="(vous sera demandé)",font=Font_desc)
    button_next = Button(frame_p,image = button_next_img_resized,width= 150,height=25,relief=FLAT,bg="#7159b5",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=tuto_3)
    button_next.place(x=575,y=450)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f62c3",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#6f60c0",text = 'précédent',compound="center",font=Font_button,command=tuto_1)
    button_prec.place(x=150,y=450)

def tuto_3():
    can.delete(ALL)
    supp_a()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="prérequis",font=Font_titre_gros)
    can.create_text(225,175,fill="white",text=f"-dans l'onglet {guillemets}Bot{guillemets} du menu à gauche\n\n       ajoutez un nouveau Bot",font=Font_desc)
    can.create_image(150,250, image=new_bot)
    can.create_text(382,322,fill="white",text=f"vous y trouverez le \n\n-activez le PRESENCE INTENT et le SERVER MEMBERS INTENT",font=Font_desc)
    can.create_text(320,300,fill="#ff7583",text=f"TOKEN du bot",font=Font_desc)
    can.create_text(475,300,fill="white",text="(vous sera demandé)",font=Font_desc)
    button_next = Button(frame_p,image = button_next_img_resized,width= 150,height=25,relief=FLAT,bg="#7159b5",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#7159b5",text = 'suivant',compound="center",font=Font_button,command=tuto_4)
    button_next.place(x=575,y=450)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="white",activeforeground="white",borderwidth=0,activebackground="#6f62c3",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#6f60c0",text = 'précédent',compound="center",font=Font_button,command=tuto_2)
    button_prec.place(x=150,y=450)

def tuto_4():
    can.delete(ALL)
    supp_a()
    can.create_image(0,0,image=linear_gradient_1)
    can.create_image(10,10,image=img_bck_white)
    can.create_text(150,50,fill="#7256B2",text="installation",font=Font_titre_gros)
    can.create_text(375,250,fill="white",text=f"vous pouvez maintenant passez à \n      l'étape de création du bot",font=Font_PyBot)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#7259b6",fg="white",activeforeground="white",borderwidth=0,activebackground="#7259b6",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=575,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#6f60c0",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#6f60c0",text = 'précédent',compound="center",font=Font_button,command=tuto_3)
    button_prec.place(x=25,y=450)

#premier menu en cliquant sur "nouveau" 
def nouveau_1():
    global ent_tok
    global ent_id
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)#UI
    can.create_image(378,235,image=ent)#UI
    can.create_text(305,140,fill="grey",text="ID de l'application",font=Font_desc)
    ent_id = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")#entrée dans laquelle on insère l'identifiant de l'app
    ent_id.place(x=225,y=150,width=300,height=50)
    can.create_text(290,260,fill="grey",text="TOKEN du Bot",font=Font_desc)
    ent_tok = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")#entrée dans laquelle on insère le token du bot
    ent_tok.place(x=225,y=270,width=300,height=50)
    button_next = Button(frame_p,image = button_open_link,width= 125,height=25,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",text = 'perdus?',compound="center",font=Font_button,command=tuto_1)
    button_next.place(x=180,y=365)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450) 
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=token_identifiant)
    button_next.place(x=600,y=450) 

#fonction du bouton suivant
def token_identifiant():
    global vect
    tok=ent_tok.get()
    ide=ent_id.get()
    if  tok != "" and ide != "":#un token/ID est une chaîne alphanumérique(uniquement numérique pour l'ID) qui ne peut pas être nulle, donc l'entrée ne peut pas être vide 
        vect=[tok,ide]
        nouveau_2()
    else:
        can.create_text(375,465,fill="red",text="le TOKEN/ID ne peut pas être nul",font=Font_desc)

def nouveau_2():
    global ent_nm
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image = linear_gradient_2)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    can.create_image(375,215,image = ent2)
    can.create_text(295,170,fill="grey",text="nom de la commande",font=Font_desc)
    ent_nm = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")
    ent_nm.place(x=200,y=185,width=350,height=50)
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=erreur_nom)
    button_next.place(x=600,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#a86cc3",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#a86cc3",text = 'précédent',compound="center",font=Font_button,command=nouveau_1)
    button_prec.place(x=150,y=450)   

def erreur_nom():#tests pour valider le nom, message d'erreur sinon
    global nom_ftn
    nom_ftn=ent_nm.get()
    if nom_ftn != "":#le nom de la fonction ne peut pas être vide, sinon l'appel de fonction est impossible 
        try:
            int(nom_ftn)        
        except:#si une erreur se produit(donc que le nom n'est pas un integer) alors le programme continue son exécution,sinon il crééra un texte sur l'écran
            nouveau_3()
        else:
            can.create_text(375,265,fill="red",text="le nom doit contenir au moins une lettre",font=Font_desc)
    else:
        can.create_text(375,465,fill="red",text="le nom ne peut pas être vide",font=Font_desc)

def nouveau_3():
    global cmd
    cmd=0
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    for i in range(10):# créé automatiquement 10 boutons avec des textes différents(rend le code plus lent mais plus lisible)
        commande = Button(frame_p,image =commande_img,width= 155,height=50,relief=FLAT,bg="#a569c2",fg="#a569c2",activeforeground="#a569c2",borderwidth=0,activebackground="#a569c2",text = 'ping @',compound="center",font=Font_button,command=lambda m=i:ftn_commande(m))#bouton de référence, modifié par la suite. la fonction lambda associe i à m et est passé en paramètre dans la fonction "ftn_commande"
        if i<=2:#permet de placer les boutons selon leur identifiant
            commande.place(x=125+(180*i),y=75)
        elif i>=3 and i<=5:
            commande.place(x=125+(180*(i-3)),y=200)
        elif i>5 and i<=8 :
            commande.place(x=125+(180*(i-6)),y=325)
        elif i == 9:
            commande.place(x=600,y=450,width = 120,height=25)      
        if i == 1:#change le paramètre "text" du bouton avec d'autres valeurs. Ainsi le paramètre "text" du 2ème bouton aura comme valeur "move"
            commande['text'] = "move @"
        elif i == 2:
            commande['text'] = "kick @"
        elif i == 3:
            commande['text'] = "ban @"
        elif i == 4:
            commande['text'] = "déconnecte @"
        elif i == 5:
            commande['text'] = "rich presence"
        elif i == 6:
            commande['text'] = "message"
        elif i == 7:
            commande['text'] = "rejoins serv"
        elif i == 8:
            commande['text'] = "nombre random"
        elif i == 9:
            commande['text'] = "suivant"
            commande['image'] = button_next_img_resized
            commande['command'] = interm
    
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#a86cc3",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#a86cc3",text = 'précédent',compound="center",font=Font_button,command=nouveau_2)
    button_prec.place(x=150,y=450)   

def interm():
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    vect_s2.append(vect_s)#ajoute la dernière fonction(paire clef valeur) au tableau vect_s2(regrouppant toutes les foncitons)
    nvx = Button(frame_p,image =commande_img_2,width= 300, height=100,relief=FLAT,bg="#a569c2",fg="#a569c2",activeforeground="#a569c2",borderwidth=0,activebackground="#a569c2",text = 'nouvelle commande',compound="center",font=Font_PyBot,command=nouveau_2)
    nvx.place(x=223,y=100)
    pref = Button(frame_p,image =commande_img_2,width= 300,height=100,relief=FLAT,bg="#a569c2",fg="#a569c2",activeforeground="#a569c2",borderwidth=0,activebackground="#a569c2",text = 'suivant',compound="center",font=Font_PyBot,command=cmd_pref)
    pref.place(x=223,y=250)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
   

def cmd_pref():
    global ent_pref
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    can.create_image(375,215,image = ent2)
    can.create_text(250,170,fill="grey",text="préfixe",font=Font_desc)
    ent_pref = Entry(frame_p,relief=SUNKEN,bg="white",font =Font_button,fg="#686868")#entrée dans laquelle on insère le préfixe
    ent_pref.place(x=200,y=185,width=350,height=50)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)     
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'génération',compound="center",font=Font_button,command=generation)
    button_next.place(x=600,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#a86cc3",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#a86cc3",text = 'précédent',compound="center",font=Font_button,command=interm)
    button_prec.place(x=150,y=450)   

#création du fichier python 
def generation():
    prefix= ent_pref.get()#récupère le préfixe entré précédemment
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    f= open("main_bot.py","w+")#créé le fichier "main_bot.py" avec l'argument "w+" signifiant write
    f.write(f"import discord\nfrom discord.ext import commands \nimport asyncio\n\nintents= discord.Intents().all()\nbot = commands.Bot(command_prefix='{prefix}', intents=intents)\n@bot.event\nasync def on_ready():\n    print('bot pret')\n")
    if act_hlp == 1:
        if c1_v.get() == 1:
            f.write(f"    await bot.change_presence(activity=discord.Game(name='{act}'))")
        if c2_v.get() == 1:
            f.write(f"    await bot.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = '{act}'))\n")
    for i in vect_s2:
        for k,v in i.items():
            if v==0:
                f.write(f"\n@bot.command()\nasync def {k}(ctx, member:discord.Member):\n   if ctx.message.author.guild_permissions.administrator==True:\n        for i in range({fois_ping}):\n            await ctx.send(member.mention)\n            await asyncio.sleep(.5)\n\n")
            if v == 1:
                f.write(f"\n@bot.command()\nasync def {k}(ctx, member: discord.Member):\n    ChannelA= bot.get_channel({chan1})\n    ChannelB= bot.get_channel({chan2})\n    if ctx.message.author.guild_permissions.move_members==True:\n        for i in range({fois_move}):\n            await member.move_to(ChannelA, reason='un utilisateur a utilise la commande de move')\n            await asyncio.sleep(1.5)\n            await member.move_to(ChannelB, reason='un utilisateur a utilise la commande de move')\n            await asyncio.sleep(1.5)\n")
            if v == 2:
                f.write(f"\n@bot.command()\nasync def {k}(ctx, member:discord.Member):\n    if ctx.message.author.guild_permissions.administrator==True:\n        await member.kick()\n\n")
            if v == 3:
                f.write(f"\n@bot.command()\nasync def {k}(ctx, member:discord.Member):\n    if ctx.message.author.guild_permissions.administrator==True:\n        await member.ban()\n\n")
            if v == 4:
                f.write(f"\n@bot.command()\nasync def {k}(ctx, member: discord.Member):\n    if ctx.message.author.guild_permissions.move_members==True:\n        for i in range({fois_deco}):\n            await member.move_to(None, reason='un utilisateur a utilise la commande de deconnection')\n            await asyncio.sleep(1.5)\n\n")
            if v == 6:
                f.write(f"\n@bot.command()\nasync def {k}(ctx):\n    await ctx.reply('{message_ftn}')\n\n")
            if v == 7:
                f.write(f"\n@bot.event\nasync def on_member_join(member):\n    await member.send(f'{message_join}')\n")
            if v == 8:
                f.write(f"\nimport random\n@bot.command()\nasync def {k}(ctx, num_un: int, num_deux: int):\n    await ctx.reply(random.randint(num_un,num_deux))\n\n")
    f.write(f"\n\nbot.run('{vect[0]}')")
    can.create_image(375,215,image = ent2)
    can.create_text(385,220,fill="#a365c1",text="bien joué, votre code est prêt!",font=Font_PyBot)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)     
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=fin)
    button_next.place(x=600,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#a86cc3",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#a86cc3",text = 'précédent',compound="center",font=Font_button,command=cmd_pref)
    button_prec.place(x=150,y=450)    

def fin():
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    can.create_image(378,235,image=ent)
    can.create_text(385,220,fill="#383c4c",text=f"les commandes {guillemets}kick{guillemets},{guillemets}ban{guillemets},\netc... fonctinnent en mentionnant l'utilisateur\naprès avoir marqué le nom de la fonction.\nLa fonction chiffre random marche en\nmettant deux chiffre servant de bordes\naprès le nom de la commande ",font=Font_desc)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=fin2)
    button_next.place(x=600,y=450)


def fin2():
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    can.create_image(378,235,image=ent)
    can.create_text(385,220,fill="#383c4c",text=f"-si vous avez pip, installez la \nbibliothèque discord.py\n\n-ouvrez un cmd et tapez la commande:\npy -3 -m pip install -U discord.py",font=Font_desc)
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#af75c7",fg="white",activeforeground="white",borderwidth=0,activebackground="#af75c7",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=25,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#a86cc3",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#a86cc3",text = 'précédent',compound="center",font=Font_button,command=fin)
    button_prec.place(x=150,y=450)
    button_next = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#9250b9",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#9250b9",text = 'suivant',compound="center",font=Font_button,command=fin3)
    button_next.place(x=600,y=450)

def fin3():
    global olhelper 
    olhelper = 2
    can.delete(ALL)
    supp_a()
    can.create_image(0,0, image= linear_gradient_2)
    can.create_image(378,235,image=ent)
    button_link= Button(frame_p,image = button_open_link,width= 150,height=25,relief=FLAT,bg="white",fg="white",activeforeground="white",borderwidth=0,activebackground="white",text = 'cliquez ici',compound="center",font=Font_button,command=open_link)
    button_link.place(x=250,y=200)
    can.create_text(385,150,fill="#383c4c",text=f"ajoutez votre Bot sur des serveurs \nen cliquant sur le bouton",font=Font_desc)
    can.create_text(375,300,fill="#383c4c",text=f"ou avec l'url:\nhttps://discord.com/api/oauth2/authorize?\nclient_id={vect[1]}&\npermissions=8&scope=bot",font=Font_desc)#le lien est personnalisé en fonction de l'indentifiant de l'applicaiton
    button_retour_home = Button(frame_p,image = button_open_link,width= 120,height=25,relief=FLAT,bg="#9250b8",fg="white",activeforeground="white",borderwidth=0,activebackground="#9250b8",text = 'Menu',compound="center",font=Font_button,command=menu_home)
    button_retour_home.place(x=590,y=450)
    button_prec = Button(frame_p,image = button_next_img_resized,width= 120,height=25,relief=FLAT,bg="#a86cc3",fg="#6e63c5",activeforeground="#6e63c5",borderwidth=0,activebackground="#a86cc3",text = 'précédent',compound="center",font=Font_button,command=fin2)
    button_prec.place(x=25,y=450)   
   

#ouvre des liens différents en fonction de la fenêtre dans laquelle le bouton est cliqué
def open_link():
    global olhelper
    if olhelper == 1:
        webbrowser.open_new("https://discord.com/developers/applications")#ouvre le portail de développeur discord si on est sur une page spécifique
    if olhelper == 2:
        webbrowser.open_new(f"https://discord.com/api/oauth2/authorize?client_id={vect[1]}&permissions=8&scope=bot")#permet d'ajouter le bot en mettant l'identifiant de l'application dans l'url

#les polices principales du programme
Font_button = font.Font(family="Abadi MT",size=14,weight="bold")#je définis la famille de la police, sa taille et si elle est(ou non) en gras
Font_PyBot = font.Font(family="Gadugi",size=22,weight="bold")
Font_desc = font.Font(family="Arial Baltic",size=14)
Font_titre = font.Font(family="Gadugi",size=16,weight="bold")
Font_titre_gros = font.Font(family="Gadugi",size=25,weight="bold")
Font_commande = font.Font(family="Arial Baltic",size=16)

#importations et modifications (si nécessaire) d'images
linear_gradent_home = PhotoImage(file="PyBot-NSI-1ere\images\linear-gradient-home.png")
button_home_img = PhotoImage(file="PyBot-NSI-1ere\images\-button-home.png")
button_home_img_resized = button_home_img.subsample(2)#reduction de la taille de l'image, en l'occurence la taille est divisée par 2
button_open_link = button_home_img.subsample(3)#divisée par 3 ici
DDPconnexion = PhotoImage(file="PyBot-NSI-1ere\images\DDP-connexion.png")
DDPconnexion_resized = DDPconnexion.subsample(2)
linear_gradient_1 = PhotoImage(file="PyBot-NSI-1ere\images\linear-gradient-1.png")
button_next_img = PhotoImage(file="PyBot-NSI-1ere\images\-button-next.png")
button_next_img_resized = button_next_img.subsample(3)
img_bck_white = PhotoImage(file="PyBot-NSI-1ere\images\prerequis.png")
new_app = PhotoImage(file="PyBot-NSI-1ere\images\-app-nvx.png")
new_bot = PhotoImage(file="PyBot-NSI-1ere\images\-bot-nvx.png")
linear_gradient_2 = PhotoImage(file="PyBot-NSI-1ere\images\linear-gradient-2.png")
ent = PhotoImage(file="PyBot-NSI-1ere\images\ent.png")   
ent = ent.subsample(2)
commande_img = PhotoImage(file="PyBot-NSI-1ere\images\commande.png")
commande_img = commande_img.subsample(2)
commande_img_2 = PhotoImage(file="PyBot-NSI-1ere\images\commande.png")
ent2 = PhotoImage(file="PyBot-NSI-1ere\images\ent-2.png")   
ent2 = ent2.subsample(2)

menu_home()#lance le menu
frame_p.mainloop()