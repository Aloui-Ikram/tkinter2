# Boucle python pour afficher le temps chaque 1s
from tkinter import *
import threading
import time 

# def horloge():
#     print('hello')
#     timer=threading.Timer(5.0, horloge)
#     timer.start()


# timer=threading.Timer(5.0, horloge)
# timer.start()




# def afficherTime():
#     localtime = time.localtime()
#     result = time.strftime("%I:%M:%S %p", localtime)
#     Texte1= Label(fenetre,text=result , fg="white", bg="#D473D4" , font=('times',20,'bold'))
#     Texte1.place(x=3, y=3)
    
# ButtonTime= Button(fenetre,text='Afficher le temps', command=afficherTime)
# ButtonTime.place(x=3, y=45)

# def afficherPic()
def afficherPic():
    buttonV=Button(fenetre, text="V", image=picV , state='disabled')
    buttonV.place(x=200,y=120)
    buttonJ=Button(fenetre,text="J", image=picJ , state='active')
    buttonJ.place(x=200,y=320)
    buttonR=Button(fenetre,text="R", image=picR , state='disabled')
    buttonR.place(x=200,y=520)
    timer2=threading.Timer(5.0 ,afficherPicR )
    timer2.start()
    
def afficherPicR():
    buttonV=Button(fenetre, text="V", image=picV , state='disabled')
    buttonV.place(x=200,y=120)
    buttonJ=Button(fenetre,text="V", image=picJ , state='disable')
    buttonJ.place(x=200,y=320)
    buttonR=Button(fenetre,text="R", image=picR , state='active')
    buttonR.place(x=200,y=520)
    
def horloge():
    buttonV=Button(fenetre,text="V", image=picV , state='active')
    buttonV.place(x=200,y=120)
    timer=threading.Timer(5.0 ,afficherPic )
    timer.start()
    
    buttonR=Button(fenetre,text="R", image=picR , state='disabled')
    buttonR.place(x=200,y=520)
    
    

fenetre = Tk()  # Creation de la fenetre principale
fenetre.title("Ma fenetre") # titre de la fenetre
fenetre.configure(width=400, height=200 , bg="#D473D4") # taille et couleur de la fenetre

Button5= Button(fenetre,text='5',command=horloge)
Button5.place(x=5,y=5)

picV=PhotoImage(file="Vert.png")
buttonV=Button(fenetre,text="V", image=picV , state='disabled')
buttonV.place(x=200,y=120)

picJ=PhotoImage(file="jaune.png")
buttonJ=Button(fenetre,text="j", image=picJ , state='disabled')
buttonJ.place(x=200,y=320)

picR=PhotoImage(file="Rouge.png")
buttonR=Button(fenetre,text="R", image=picR , state='disabled')
buttonR.place(x=200,y=520)

fenetre.mainloop() #maintenir la fenetre ouverte