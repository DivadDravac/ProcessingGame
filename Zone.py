import random
import math

class Zone:
    def __init__(self):
        self.cartesExectutees = -1
        self.Stop = 0
        self.cartes = []

    def IsCarte(self, carte):
        #print(carte)
        return carte in self.cartes
    
    def ExecuterFonctions(self, ToExecute, Carte):
        
        while self.cartesExectutees > -1:# arret de l boucle lorsque besoin
            if self.cartes[self.cartesExectutees].ExecuterFonction(ToExecute, Carte):
                
                self.cartesExectutees = cartesExectutees - 1

                if ToExecute == "Execute" :
                    #si un objet sur le bord sinon defausse
                    if Carte.activation == 0:
                        self.zones["Defausse"].Move(self.cartes[self.cartesExectutees], self)
                    else:
                        if Carte.joueur == 0:
                            self.zone["J1Terr"].Move(self.cartes[self.cartesExectutees], self)
                        else:
                            self.zone["J2Terr"].Move(self.cartes[self.cartesExectutees], self)
                else:
                    pass

            else:
                return False

        return True


    def ResetZone(self):
        self.cartesExectutees = len(self.cartes) - 1
        for CartesReset in self.cartes:
            CartesReset.Reset()

    def Move(self, Cible, From):
        Cible.zoneActuelle = self
        self.AjoutCarte(Cible)
        print(From, Cible)
        From.cartes.remove(Cible)


class Main(Zone):
    def __init__(self, Joueur):
        Zone.__init__(self)
        self.joueur = Joueur


    def AjoutCarte(self, Carte):
        Carte.joueur = self.joueur
    
        if Carte.joueur.numero == 1:
            Carte.face = 1
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

        if self.joueur.numero == 1:
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
        
    def AjoutCarte(self, Carte):
        
        Pos = [0,0]
        Angle = 0
        Carte.face = 1
        
        if Carte != 0:
            self.cartes.append(Carte)
            if Carte.joueur.numero == 1:
                Pos = [300 + len(self.cartes)*50, 370]
                
            else:
                Pos = [300 + len(self.cartes)*50, 320]
                Angle = 180

            Carte.SetPos(Pos, Angle,0.5)
            

        
class Defausse(Zone):
    def __init__(self, Joueurs):
        Zone.__init__(self)
        self.joueurs = Joueurs

    def AjoutCarte(self, Carte):
        if Carte != 0:
            if self.joueurs[0].Terr.ExecuterFonctions("Defausse"):
                if self.joueurs[0].Terr.ExecuterFonctions("Defausse"):

                    Pos = [800 + random.randint(0, 100),350 + random.randint(0, 100)]
                    Angle = random.randint(0, 360)
                    
                    Carte.SetPos(Pos, Angle,0.5)
                    self.cartes.append(Carte)
        

class Bibliotheque(Zone):

    def Piocher(self, Joueur, Hasard = False):
        if len(self.cartes) > 0:
            if Joueur.Terr.ExecuterFonctions("Pioche", 0):
                cartePiochee = 0
                if Hasard:
                    randIndex = random.randint(0, len(self.cartes)-1)
                    cartePiochee = self.cartes[randIndex]
                else:
                    cartePiochee = self.cartes[len(self.cartes)-1]
                Joueur.Main.Move(cartePiochee, self)
                return cartePiochee
            else:
                return -1

        else:
            return False
    
    def SetBibliotheque(self,Bib):
        self.cartes = Bib.copy()
        for c in self.cartes:
            c.zoneActuelle = self
            c.SetPos([50,350], 90, 0.5)