from PIL import Image, ImageDraw, ImageFont
import os
import JeuN1 as Jeu
import Carte

Circuit = 0
Prise2 = 1
Prise4 = 2
Prise8 = 3 
Chip6 = 4
Chip16 = 5
MicropB = 6
PicropEx = 7
Nom = 8
LedB0 = 9
LedB1 = 10
LedR0 = 11
LedR1 = 12

TableauCartes = []
im = []
font = ImageFont.truetype('computer_pixel-7.ttf', 30)   

def MicroP(Numero):
    if Numero == -1:
        CarteImg.paste(im[PicropEx], (184, 75), im[PicropEx])
        CarteImg.paste(im[Prise8], (176, 0), im[Prise8])
    elif Numero == 0:
        CarteImg.paste(im[Prise2], (0, 24), im[Prise2])
        CarteImg.paste(im[MicropB], (91, 60+66*3), im[MicropB])
    else:
        CarteImg.paste(im[Prise4], (0, 58+66*Numero), im[Prise4])
        CarteImg.paste(im[Chip6], (37, 65+66*Numero), im[Chip6])
        CarteImg.paste(im[Chip16], (96, 67+66*Numero), im[Chip16])
    


#Lit le dossier
for path in Jeu.FichiersCartes:
    #Traite le mon de la carte

    CarteNom = path.split("$")[0]
    CarteType = path.split("$")[1]
    CarteActivation = int(path.split("$")[2])
    CarteFonction = path.split("$")[3]
    opencard = Carte.Carte(CarteNom, CarteActivation, CarteFonction, "ComposantsCarte/Circuit.png" , CarteType,0,{})
    
    TableauCartes.append(opencard)
    

for imFile in os.listdir("ComposantCartesSep/"):
    print(imFile)
    im.append(Image.open("ComposantCartesSep/"+ imFile))


## Création des cartes
for carte in TableauCartes:
    CarteImg = im[0].copy()#Circuit<
    
    if carte.fonctions["Debut"]["Fct"] != '':
        MicroP(1)
    if carte.fonctions["Pioche"]["Fct"] != '':
        MicroP(2)
    if carte.fonctions["Joue"]["Fct"] != '':
        MicroP(0)
    if carte.fonctions["Execute"]["Fct"] != '':
        MicroP(-1)
    if carte.fonctions["Fin"]["Fct"] != '':
        MicroP(3)
    if carte.fonctions["Defausse"]["Fct"] != '':
        MicroP(4)

    CarteImg.paste(im[Nom], (64, 18), im[Nom])

    carac = ImageDraw.Draw(CarteImg)                                  
    carac.text((75,27), carte.nom, font=font, fill=(255,255, 255) ) 

    CarteImg.save("test/"+carte.nom+".png")

