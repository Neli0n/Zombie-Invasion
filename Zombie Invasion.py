# #####################################
# ###### Projet ISN 2018-2019 #########
# ###### Lycée Pierre d'Ailly #########
# ########## Dorian Coupé #############
# ######### Teddy Mouaffo #############
# ######## Zombie Invasion ############
# #####################################

# #####################################
#
import pygame,sys,random
from pygame.locals import *    #Importation
import pygame as pg

# Ennemi et Tank
Ennemi=pygame.image.load("Ennemi.png")
Tank=pygame.image.load("Tank.png")



xMaxEnnemi = 1300
xMinEnnemi = 50
yMinEnnemi = 50
yMaxEnnemi = 600
NbZombies=10

pygame.init()
pygame.display.set_caption('TMDC') #Initialisation Fenêtre
fen=pygame.display.set_mode((1407,737))
fond = pygame.image.load("Plan de jeu.png")
fen.blit(fond,(0,0))

###########################################
# Son ambiance
son2 = pygame.mixer.Sound("ambiance.wav")
son2.play(-1) #joue le son2 en boucle.
rectTank=fen.blit(Tank,(1360,690))


pygame.display.update

def ListeCoordsZombies():
    liste=[]
    for i in range(NbZombies):
        x=random.randint(xMinEnnemi,xMaxEnnemi)
        y=random.randint(yMinEnnemi,yMaxEnnemi)
        liste.append([x,y])
    return liste
LCZ=ListeCoordsZombies()


def affiche():
    for i  in range(NbZombies):
        fen.blit(Ennemi,(LCZ[i][0],LCZ[i][1]))
fin=0
def collision():
    for i in range(NbZombies):

        rectEnnemiG=fen.blit(Ennemi,(LCZ[i][0],LCZ[i][1]))
        if rectTank.colliderect(rectEnnemiG)==True:
            LCZ[i][0]+=1000000
            global fin
            fin=fin+1
            print(fin)




fen.blit(Tank,rectTank)
pygame.display.update()
while True:
        pygame.key.set_repeat(40,20)
        collision()
        for evenement in pygame.event.get():
            if evenement.type==QUIT:
                pygame.quit()
                sys.exit

            if evenement.type==KEYDOWN:
                listeTouche = pygame.key.get_pressed()
                if listeTouche[K_RIGHT]:
                     if rectTank.x<1400:
                      rectTank.x=rectTank.x+25
                if listeTouche[K_LEFT]:
                     if rectTank.x>10:
                        rectTank.x=rectTank.x-25
                if listeTouche[K_UP]:
                     if rectTank.y>10:
                        rectTank.y=rectTank.y-25
                if listeTouche[K_DOWN]:
                    if rectTank.y<700:
                     rectTank.y=rectTank.y+25
            fen.blit(fond,(0,0))
            affiche()
            fen.blit(Tank,rectTank)
            pygame.display.update()
            if fin==10:
                pygame.display.quit()
                sys.exit
                print ("Félicitation, vous avez gagné !")



            #Mise Ã  jour de l'affichage









