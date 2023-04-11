import Carte
import os
import random

class Chargeur:
    def __init__(self, Zones):
        self.TableauCartes = []
        self.zones = Zones

    def Init(self, NomFichier = ""):
        #Lit le dossier
        for path in os.listdir(NomFichier):
            #Traite le mon de la carte

            CarteNom = path.split("$")[0]
            CarteType = path.split("$")[1]
            CarteActivation = int(path.split("$")[2])
            CarteFonction = path.split("$")[3]
            CarteImage = path
            opencard = Carte.Carte(CarteNom, CarteActivation, CarteFonction, NomFichier + "/" + CarteImage, CarteType,0, self.zones)
            
            self.TableauCartes.append(opencard)
            
        self.TableauCartes = self.Shuffle(self.TableauCartes)

        return self.TableauCartes

    def Shuffle(self,TabCartes):
        newTab = []
        for index in range(len(TabCartes)):
            
            CarteShuffledNb = random.randint(0, len(TabCartes)-1)

            newTab.append(TabCartes[CarteShuffledNb])
            TabCartes.remove(TabCartes[CarteShuffledNb])
            
        return newTab

