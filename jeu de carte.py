import pygame
import Board
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()

battleReady = Board.Board("Biblio")

CarteAffiche = [battleReady.Defausse.cartes,
                battleReady.Bibliotheque.cartes,
                battleReady.Proc.cartes,
                battleReady.Joueur1.Main.cartes,
                battleReady.Joueur1.Terr.cartes,
                battleReady.Joueur2.Main.cartes,
                battleReady.Joueur2.Terr.cartes]

def PlaceImage(Carte):

    Pos = (0,0)
    ImageScale = pygame.transform.scale_by(Carte.image, Carte.echelleBuff)
    ImageRot = pygame.transform.rotate(ImageScale, Carte.angleBuff )
    Pos = (Carte.posBuff[0]-ImageRot.get_width()/2, Carte.posBuff[1]-ImageRot.get_height()/2)
    Image = screen.blit(ImageRot,Pos)
    #print((Carte.posBuff[0]-ImageRot.get_width()/2, Carte.posBuff[1]-ImageRot.get_height()/2))
    return Image

def UpdateScreen():
    CartesToUpdate = []
    
    screen.fill((255, 255, 255))
    for CartesZone in CarteAffiche:
        for Carte in CartesZone:
            CartesToUpdate.append([Carte, PlaceImage(Carte)])

    pygame.display.flip()
    clock.tick(60)
    return CartesToUpdate

def StartGame():

    BufCarte = 0
    BufSelect = 0
    Cartes = UpdateScreen()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                BufSelect = 0
                ## if mouse is pressed get position of cursor ##
                for CardPloted in Cartes:
                    if CardPloted[1].collidepoint(pos):
                        BufSelect = CardPloted
                if BufSelect != 0:
                    battleReady.SelectionneCarte(BufSelect[0])
                    
            if e.type == pygame.MOUSEMOTION:
                BufCarte = 0
                for CardPloted in Cartes:
                    if CardPloted[1].collidepoint(pos):
                        BufCarte = CardPloted       
        else:
            
            if BufCarte != 0:
                if not battleReady.Bibliotheque.IsCarte(BufCarte[0]) and not battleReady.Defausse.IsCarte(BufCarte[0]):
                    for CardPloted in Cartes:
                        if CardPloted == BufCarte:
                            CardPloted[0].Select(True)
                        else:
                            CardPloted[0].Select(False)
            else:
                for CardPloted in Cartes:
                    CardPloted[0].Select(False)
            Cartes = UpdateScreen()

StartGame()