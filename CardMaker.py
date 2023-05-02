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
fontNb = ImageFont.truetype('computer_pixel-7.ttf', 20)   


def MicroP(Numero, fct, activation = 0, IsJoue = False):
    if Numero == -1:
        #Prise
        CarteImg.paste(im[Prise8], (176, 0), im[Prise8])

        ChipBuf = PrintFctExec(fct)

        CarteImg.paste(ChipBuf, (184,75), ChipBuf)
        

    else:
        if IsJoue:
            #Prise
            CarteImg.paste(im[Prise2], (0, 24), im[Prise2])

            #microchip
            ChipBuf = PrintFct(fct)
            CarteImg.paste(ChipBuf[0], (ChipBuf[1][0], ChipBuf[1][1]+ChipBuf[1][2]*Numero), ChipBuf[0])

            #LED
            CarteImg.paste(im[LedR1], (61, 157+ChipBuf[1][2]*(Numero-1)), im[LedR1])

        else:
            #Prise
            CarteImg.paste(im[Prise4], (0, 58+66*Numero), im[Prise4])

            #LED
            CarteImg.paste(im[LedB1], (40, 166+66*(Numero-1)), im[LedB1])

            #Compteur de marqueur
            Chip = im[Chip6].copy()
            carac = ImageDraw.Draw(Chip)                                  
            carac.text((13,0), str(activation), font=fontNb, fill=(255,255, 255) ) 
            CarteImg.paste(Chip, (37, 65+66*Numero), Chip)

            #microchip
            ChipBuf = PrintFct(fct)
            CarteImg.paste(ChipBuf[0], (ChipBuf[1][0], ChipBuf[1][1]+ChipBuf[1][2]*Numero), ChipBuf[0])

def PrintFctExec(fct):
    Chip = im[PicropEx].copy()
    fctList = fct.split("¤")
    fctList.remove("")
    carac = ImageDraw.Draw(Chip)  

    if len(fctList)>0:
        carac.text((120,-5),fctList[0], font=font, fill=(255,255, 255) ) 
    if len(fctList)>1:
        carac.text((70,4),fctList[1], font=font, fill=(255,255, 255)) 
    if len(fctList)>2:
        carac.text((13,20),fctList[2], font=font, fill=(255,255, 255)) 

    return Chip.rotate(-90, expand=1)

def PrintFct(fct):

    fctList = fct.split("¤")
    fctList.remove("")
    Delta = (0,0,0)
                      
    if len(fctList) > 1:
        Chip = im[MicropB].copy()
        Delta = (91, 62, 65)
        carac = ImageDraw.Draw(Chip)  
        i=0
        for f in fctList:   
          if f != "":
            carac.text((10,9+i*20),f, font=font, fill=(255,255, 255) ) 
            i = i+1

    else:
        Chip = im[Chip16].copy()
        carac = ImageDraw.Draw(Chip)  
        Delta = (96, 69, 65)
                                        
        carac.text((10,8),fctList[0], font=font, fill=(255,255, 255) ) 


    return (Chip,Delta)


#Lit le dossier
for path in Jeu.FichiersCartes:
    #Traite le mon de la carte

    CarteNom = path.split("$")[0]
    CarteType = path.split("$")[1]
    CarteActivation = int(path.split("$")[2])
    CarteFonction = path.split("$")[3]
    CarteImg = Image.open("ComposantsCarte/Circuit.png")
    CarteImg.save("test/"+path)
    opencard = Carte.Carte(CarteNom, CarteActivation, CarteFonction, "test/"+path , CarteType,0,{})
    
    TableauCartes.append(opencard)
    

for imFile in os.listdir("ComposantCartesSep/"):
    print(imFile)
    im.append(Image.open("ComposantCartesSep/"+ imFile))


## Création des cartes
for carte in TableauCartes:
    CarteImg = im[0].copy()#Circuit<
    
    if carte.fonctions["Debut"]["Fct"] != '':
        MicroP(0, carte.fonctions["Debut"]["Fct"], carte.activation)
    if carte.fonctions["Pioche"]["Fct"] != '':
        MicroP(1, carte.fonctions["Pioche"]["Fct"], carte.activation)
    if carte.fonctions["Joue"]["Fct"] != '':

        if carte.fonctions["Debut"]["Fct"] == "":
            MicroP(0, carte.fonctions["Joue"]["Fct"],IsJoue=True)
        elif carte.fonctions["Pioche"]["Fct"] == "":
            MicroP(1, carte.fonctions["Joue"]["Fct"],IsJoue=True)
        elif carte.fonctions["Fin"]["Fct"] == "":
            MicroP(2, carte.fonctions["Joue"]["Fct"],IsJoue=True)
        elif carte.fonctions["Defausse"]["Fct"] == "":
            MicroP(3, carte.fonctions["Joue"]["Fct"],IsJoue=True)
        

    if carte.fonctions["Execute"]["Fct"] != '':
        MicroP(-1, carte.fonctions["Execute"]["Fct"])
    if carte.fonctions["Fin"]["Fct"] != '':
        MicroP(2, carte.fonctions["Fin"]["Fct"], carte.activation)
    if carte.fonctions["Defausse"]["Fct"] != '':
        MicroP(3, carte.fonctions["Defausse"]["Fct"], carte.activation)

    CarteImg.paste(im[Nom], (64, 18), im[Nom])

    carac = ImageDraw.Draw(CarteImg)                                  
    carac.text((75,27), carte.nom, font=font, fill=(255,255, 255) ) 

    CarteImg.save(carte.imagePath)

