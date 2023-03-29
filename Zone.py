import random
import math

class Zone:
    def __init__(self):
        self.cartesExectutees = 0
        self.Stop = 0
        self.cartes = []

    def IsCarte(self, carte):
        #print(carte)
        return carte in self.cartes
    
    def ExecuterFonctions(self, ToExecute, Carte):
        if self.cartesExectutees == 0:
            self.cartesExectutees = len(self.cartes) - 1 

        if self.cartesExectutees != -1:
            while self.cartes[self.cartesExectutees].ExecuterFonction(ToExecute):# arret de l boucle lorsque besoin
                self.cartesExectutees = cartesExectutees - 1
                self.zones[Defausse].append(cartesExecute)
                self.cartes.remove(cartesExecute)

        if self.cartesExectutees == -1:
            return True
        else:
            return False

    def ResetZone(self):
        self.cartesExectutees = len(self.cartes) - 1
        for CartesReset in self.cartes:
            CartesReset.Reset()


class Main(Zone):
    def __init__(self, Joueur):
        Zone.__init__(self)
        self.joueur = Joueur


    def AjoutCarte(self, Carte):
        Carte.joueur = self.joueur
        self.cartes.append(Carte)
        self.UpdateMain()
        
  
    def UpdateMain(self):
        maxCarte = len(self.cartes)
        Y = 0
        X = 0
        Offset = 350
        Ech = 0
        Ang = 0
        AngOffset = 0
        Ligne = 0

        if self.joueur == 1:
            X = 500
            Y = 770
            Ech = 1
            Ang = 1
        else:
            X = 500
            Y = 0
            Ech = 0.7 
            Ang = -1
            AngOffset = 180
            
        for C in range(len(self.cartes)):
            #print (self.cartes[C].nom, [ Offset + X*C/maxCarte, Y - 200*(math.sin(self.cartes[C].angle))/2],  Ang*(15-40*C/maxCarte), Ech)
            self.cartes[C].SetPos([ Offset + X*C/maxCarte, Y] ,  Ang*(15-40*C/maxCarte)+AngOffset, Ech)
          


class Terrain(Zone):
    def AjoutCarte(self):
        pass

class Processeur(Zone):
        
    def ExecuterLaPile(self):
        self.cartesExectutees = len(self.cartes)-1
        if len(self.cartes) > 0:
            if self.cartes[self.cartesExectutees].ExecuterFonction("Execute"):
                #print(self.cartes[self.cartesExectutees].zones)
                self.cartes[self.cartesExectutees].zones["Defausse"].AjoutCarte(self.cartes[self.cartesExectutees])
                self.cartes.remove(self.cartes[self.cartesExectutees])
                print("Execution Suivante")
                return self.ExecuterLaPile()
            else:
                print("Arret d'execution")
                return False
        else:
            print("plus rien à executer")
            return True
    
    def AjoutCarte(self, Carte):
        
        Pos = [0,0]
        Angle = 0

        if Carte != 0:
            if Carte.joueur == 1:
                Pos = [300 + len(self.cartes)*50, 370]
            else:
                Pos = [300 + len(self.cartes)*50, 320]
                Angle = 180
            Carte.SetPos(Pos, Angle,0.7)
            self.cartes.append(Carte)

        
class Defausse(Zone):
    def AjoutCarte(self, Carte):
        
        Pos = [800 + random.randint(0, 100),350 + random.randint(0, 100)]
        Angle = random.randint(0, 360)

        if Carte != 0:
            Carte.SetPos(Pos, Angle,0.7)
            self.cartes.append(Carte)
        

class Bibliotheque(Zone):

    def Piocher(self):
        if len(self.cartes) > 0:
            randIndex = random.randint(0, len(self.cartes)-1)
            CarteHazard = self.cartes[randIndex]
            self.cartes.remove(CarteHazard)
            return CarteHazard
        else:
            return 0
    
    def SetBibliotheque(self,Bib):
        self.cartes = Bib.copy()
        for c in self.cartes:
            c.SetPos([50,350], 90, 0.7)