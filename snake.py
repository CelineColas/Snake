# SNAKE != SNACK

# ATTRAPE lA BOULE ROUGE
# EVITE LES BOULES BLEUES
# EVITE LES BORDS
# EVITE DE TE RENTRER DEDANS

# UTILISES LES FLECHES DIRECTIONNELLES POUR TE DIRIGER
# MAINTIENS LA BARRE ESPACE POUR ALLER PLUS VITE (attention, le serpent s allonge et prend donc plus de place)

# Le serpent se met a bouger automatiquement après 2 secondes
# Il faut cliquer sur la fenetre pour que les touches soient detectees
# Le jeu se ferme automatiquement 5 secondes apres le game over

from tkinter import*
import time
from random import randrange

fen=Tk()
can=Canvas(height=250,width=250,bg="black")
can.pack()

# # # # # Variables # # # # #

debut=False
perdu=False

cou_snake="white"
cou_piece="red"
cou_piege="blue"

sens="horizontal"
direction="gauche"

score=0 ### Permet de compter le score
balise=0 ### Permet d avoir des paliers
speed=1 ### Permet de changer la "vitesse"
t_s=1 ### Taille serpent
t_p=5 ### Taille piece
t_x=5 ### Taille pieges
hauteur=250
largeur=250
X=-1 ### Valeurs de départ
Y=0  ### car il part par la gauche

co_piege=[] ### Coordonnees des pieges
pieges=[] ### Pieges : objets
corps_snake=[] ### Corps serpent : objet
pos_alea=[-2,+2,0,0] ### Positions possibles aleatoire pour le deplacement des pieges

# # # # # # # # # # # # # # #

# # # # # # Placement Piece # # # # # # # #

a=randrange(t_p+2,largeur-t_p-2) ### Random pour le x
b=randrange(t_p+2,hauteur-t_p-2) ### Random pour le y

co_piece=[ ### Definition coordonnes piece en fonction de x et y
            a-t_p,
            b-t_p,
            a+t_p,
            b+t_p]

piece=can.create_oval( ### Creation de la 1ere piece : objet
                        a-t_p,
                        b-t_p,
                        a+t_p,
                        b+t_p,
                        fill=cou_piece,
                        outline=cou_piece)

# # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # Creation Serpent # # # # # # # # # # # #

pos_snake=[[largeur/2,hauteur/2]] ### Creation position tete serpent

for i in range(50): ### Creation coordonnees corps serpent
    pos_snake.append([largeur/2+t_s*2*(i+1),hauteur/2])

for i in range(50): ### Creation corps serpent : objet
    corps_snake.append(can.create_oval(
                                        pos_snake[i][0]-t_s,
                                        pos_snake[i][1]-t_s,
                                        pos_snake[i][0]+t_s,
                                        pos_snake[i][1]+t_s,
                                        fill=cou_snake,
                                        outline=cou_snake)
                                        )

snake=can.create_oval( ### Creation tete serpent : objet
                        pos_snake[0][0]-t_s,
                        pos_snake[0][1]-t_s,
                        pos_snake[0][0]+t_s,
                        pos_snake[0][1]+t_s,
                        fill=cou_snake,
                        outline=cou_snake)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # Fonction  # # # # # # #

def verif_collision(): ### Verifie s il ne touche pas un bord ou lui-meme
    global save2,test,perdu
    if pos_snake[0][0]+t_s +(2*X)*speed <largeur : ### Si depasse pas a droite
        if pos_snake[0][0]-t_s +(2*X)*speed >0 : ### Si depasse pas a gauche
            if pos_snake[0][1]-t_s +(2*Y)*speed <hauteur : ### Si depasse pas en bas
                if pos_snake[0][1]+t_s +(2*Y)*speed > 0 : ### Si depasse pas en haut
                    save2= [pos_snake[0][0]+(2*X)*speed,pos_snake[0][1]+(2*Y)*speed] ### Sauve nouvelle valeur de la tête
                    test=True ### indique qu il y a une une modif

    for i in range(len(pos_snake)-1): ### Si le serpent se touche lui-meme
        if pos_snake[i+1][0]-t_s*2<pos_snake[0][0]<pos_snake[i+1][0]+t_s*2:
            if pos_snake[i+1][1]-t_s*2<pos_snake[0][1]<pos_snake[i+1][1]+t_s*2:
                perdu=True

    for i in range(len(co_piege)): ### On verifie que le serpent ne se prend pas un piege
        if co_piege[i][0]-t_s +(2*X)*speed <pos_snake[0][0]<co_piege[i][2]+t_s+(2*X)*speed :
            if  co_piege[i][1]-t_s+(2*X)*speed<pos_snake[0][1]<co_piege[i][3]+t_s+(2*X)*speed :
                perdu=True

    if test!=True:
        perdu=True

def avancer():
    global pos_snake,co_piece,perdu,score,piege,balise,pieges,co_piege,test
    test=False
    if score>=5+balise: ### Si on atteint un multiple de 5 dans le score
        balise=score

        a=randrange(t_x+2,largeur-t_x-2)
        b=randrange(t_x+2,hauteur-t_x-2)
        co_piege.append([a-t_x,b-t_x,a+t_x,b+t_x]) ### Ajout coordonnees piege supplementaire
        pieges.append(can.create_oval( ### Creation piege : objet
                                        a-t_x,
                                        b-t_x,
                                        a+t_x,
                                        b+t_x,
                                        fill=cou_piege,
                                        outline=cou_piege)
                                        )

    if len(co_piege)>0: ### Si il existe des pieges
        for i in range(len(co_piege)):
            a=randrange(0,4) ## Choix
            b=randrange(0,4) ## Coordonnees
            if co_piege[i][0]+pos_alea[a]>0: ### Si le piege ne va pas sortir de la fenetre
                if co_piege[i][1]+pos_alea[b] >0:
                    if co_piege[i][2]+pos_alea[a] < largeur :
                        if co_piege[i][3]+pos_alea[b]<hauteur:
                            co_piege[i]=[ ### Le piege prend de nouvelles coordonnees
                                        co_piege[i][0]+pos_alea[a],
                                        co_piege[i][1]+pos_alea[b],
                                        co_piege[i][2]+pos_alea[a],
                                        co_piege[i][3]+pos_alea[b]]

            can.coords( ### Le piege change de palce
                        pieges[i],
                        co_piege[i][0],
                        co_piege[i][1],
                        co_piege[i][2],
                        co_piege[i][3])

    verif_collision() ### Verifie qu il n y a pas de collision

    if test==True: ### Si le serpent n est pas mort
        i=0
        save=pos_snake ### Sauvegarde de la position actuelle - la new position de la tête
        pos_snake=[save2]

        while i < len(save)-1 : ### La position d un point du serpent prend la precedente position du point qui le precede
            pos_snake.append(save[i])
            i+=1
        can.coords( ###  On actualise la position de la tete egalement
                    snake,
                    pos_snake[0][0]-t_s,
                    pos_snake[0][1]-t_s,
                    pos_snake[0][0]+t_s,
                    pos_snake[0][1]+t_s)
        i=1

        while i < len(pos_snake) : ### Le corps du serpent prend ses nouvelles positions
            can.coords(
                        corps_snake[i-1],
                        pos_snake[i][0]-t_s,
                        pos_snake[i][1]-t_s,
                        pos_snake[i][0]+t_s,
                        pos_snake[i][1]+t_s)
            i+=1

        if co_piece[0]-t_s<pos_snake[0][0]<co_piece[2]+t_s : ### Si on mange la piece
            if co_piece[1]-t_s<pos_snake[0][1]<co_piece[3]+t_s :
                score+=1
                a=randrange(t_p+5,largeur-t_p-5)
                b=randrange(t_p+5,hauteur-t_p-5)

                can.coords( ### alors elle change de place
                            piece,
                            a-t_p,
                            b-t_p,
                            a+t_p,
                            b+t_p)

                co_piece=[ ### Enregistrement des new coordonnees
                            a-t_p,
                            b-t_p,
                            a+t_p,
                            b+t_p]

                for i in range(10): ### On ajoute des points a la queue du serpent
                    pos_snake.append([
                                        pos_snake[len(pos_snake)-1][0],
                                        pos_snake[len(pos_snake)-1][1]])

                    corps_snake.append(can.create_oval(
                                                        pos_snake[len(pos_snake)-1][0]-t_s,
                                                        pos_snake[len(pos_snake)-1][1]-t_s,
                                                        pos_snake[len(pos_snake)-1][0]+t_s,
                                                        pos_snake[len(pos_snake)-1][1]+t_s,
                                                        fill=cou_snake,
                                                        outline=cou_snake)
                                                        )
                for i in range(10): ### On les met en place
                    can.coords(
                                corps_snake[len(corps_snake)-11+i],
                                pos_snake[len(corps_snake)-10+i][0]-t_s,
                                pos_snake[len(corps_snake)-10+i][1]-t_s,
                                pos_snake[len(corps_snake)-10+i][0]+t_s,
                                pos_snake[len(corps_snake)-10+i][1]+t_s)

    fen.after(10,go)


def go(): ### Si on a pas perdu, le serpent continue d avancer
    global debut
    debut=True
    if perdu==False:
        avancer()
    else:
        texte=str ("Ton score est de " + str(score))
        noir=can.create_rectangle(0,0,largeur,hauteur,fill="black",stipple="gray50")
        can.create_text(hauteur/2,largeur/2,text="PERDU !",fill="red",font="Comic 30")
        can.create_text(hauteur/2,largeur/2+50,text=texte,fill="red",font="Comic 15")
        fen.after(4000,fen.destroy)

def boost(event): ### Augmente la vitesse du serpent
    global speed
    if debut==True:
        speed=2

def nonboost(event): ### Diminue la vitesse du serpent
    global speed
    if debut==True:
        speed=1

def demarrer(): ### Demarre le jeu
    if debut==False:
        go()

# # # # # Gestion directions # # # # #

def k_up(event):
    global direction,speed,X,Y
    if debut==True and direction!="bas":
        direction="haut"
        X=0
        Y=-1

def k_down(event):
    global sens,direction,speed,X,Y
    if debut==True and direction!="haut":
        direction="bas"
        X=0
        Y=1

def k_left(event):
    global sens,direction,speed,X,Y
    if debut==True and direction!="droite":
        direction="gauche"
        X=-1
        Y=0

def k_right(event):
    global sens,direction,speed,X,Y
    if debut==True and direction!="gauche":
        direction="droite"
        X=1
        Y=0


# # # # # # # # # # # # #  # # # # #

# # # # Gestion d evenements # # # #

fen.bind("<Up>",k_up)
fen.bind("<Down>",k_down)
fen.bind("<Left>",k_left)
fen.bind("<Right>",k_right)
fen.bind("<KeyRelease-space>",nonboost)
fen.bind("<space>",boost)

# # # # # # # # # # # # # # # # # # #

fen.after(2000,demarrer) ### Lancement du jeu automatique apres 2 secondes

fen.mainloop()
