import pygame

class Carte:
    def __init__(self, CarteNom = "Default", CarteFonction ="", CarteImage = "", CarteType = "", CarteJoueur = "", ZonesCartes = {}):
        
        #InitCarte
        self.face = 0
        self.nom = CarteNom
        self.imagePath = CarteImage
        self.type = CarteType
        self.joueur = CarteJoueur
        self.image = pygame.image.load(CarteImage)
        self.zones = ZonesCartes
        self.fonctions = {}

        Fonctions = CarteFonction.split("&")
        if len(Fonctions) > 0:
            self.fonctions ["Debut"] = {"Fct":Fonctions[0],"State": 0,"Act": 0}
        else:
            self.fonctions ["Debut"] = {"Fct":"","State": 0,"Act": 0}
        
        if len(Fonctions) > 1:
            self.fonctions ["Pioche"] = {"Fct":Fonctions[1],"State": 0,"Act": 0}
        else:
            self.fonctions ["Pioche"] = {"Fct":"","State": 0,"Act": 0}
            
        if len(Fonctions) > 2:
            self.fonctions ["Joue"] = {"Fct":Fonctions[2],"State": 0,"Act": 0}
        else:
            self.fonctions ["Joue"] = {"Fct":"","State": 0,"Act": 0}

        if len(Fonctions) > 3:
            self.fonctions ["Execute"] = {"Fct":Fonctions[3],"State": 0,"Act": 0}
        else:
            self.fonctions ["Execute"] = {"Fct":"","State": 0,"Act": 0}
        
        if len(Fonctions) > 4:
            self.fonctions ["Fin"] = {"Fct":Fonctions[4],"State": 0,"Act": 0}
        else:
            self.fonctions ["Fin"] = {"Fct":"","State": 0,"Act": 0}
        
        if len(Fonctions) > 5:
            self.fonctions ["Defausse"] = {"Fct":Fonctions[5],"State": 0,"Act": 0}
        else:
            self.fonctions ["Defausse"] = {"Fct":"","State": 0,"Act": 0}

        #Props
        self.marqueur = 0
        self.pos = [0,0]
        self.angle = 0
        self.echelle = 1
        self.selected = False
        self.target = 0
        
        self.echelleBuff = 0
        self.posBuff = [0,0]
        self.angleBuff = 0
        self.Trans = 1
        
    #Set position Tien compte de la dynamique
    def SetPos(self, PosToSet, AngleToSet, ScaleToSet):
        #self.posBuff = PosToSet
        #self.angleBuff = AngleToSet
        #self.echelleBuff = ScaleToSet
        self.pos = PosToSet
        self.angle = AngleToSet
        self.echelle = ScaleToSet

    #Mise en avant de la carte
    def Select(self, IsSelected):

        if IsSelected != self.selected and IsSelected == True:
            self.selected = True

        if self.selected and self.Trans < 100:
            self.Trans = self.Trans + 10
        elif self.selected and self.Trans >= 100:
            self.selected = False
        elif  self.Trans > 1 and self.selected == False:
            self.Trans = self.Trans - 10

        self.posBuff = [1080/2 * self.Trans/100 + self.pos[0] * (1-self.Trans/100),720/2* self.Trans/100 + self.pos[1] * (1-self.Trans/100)]
        self.echelleBuff = 1.5 * self.Trans/100 + self.echelle * (1-self.Trans/100)
        self.angleBuff = self.angle * (1-self.Trans/100)

    #Execute la fonction appropriée
    def ExecuterFonction(self,ToExecute):
        if ToExecute != "Execute" and self.marqueur > self.fonctions[ToExecute]["Act"]:
            if self.ExecuteSeq(self.fonctions[ToExecute]["Fct"]):
                return True
            else:
                return False
        elif ToExecute == "Execute":
            if self.ExecuteSeq(self.fonctions[ToExecute]["Fct"]):
                return True
            else:
                return False

    def GetCible(self, Step):

        if Step == '=':#Biblio
            Cible = self.zones["Biblio"]

        elif Step == '#':#Selection
            if self.target != 0:
                Cible = self.target

        elif Step == '?':#Rand
            ZoneCible = random.choice(self.zones.items())
            Cible = random.choice(self.zones[ZoneCible].cartes)

        elif Step == 'P':#ToutProc
            Cible = self.zones["Proc"]

        elif Step == 'D':#ToutDef
            Cible = self.zones["Defausse"]

        elif Step == 'T' :#ToutTerrJ1
            if Joueur == 1:
                Cible = self.zones["J1Terr"]
            else :
                Cible = self.zones["J2Terr"]

        elif Step == 't':#ToutTerrJ2
            if Joueur == 1:
                Cible = self.zones["J2Terr"]
            else :
                Cible = self.zones["J1Terr"]

        elif Step == 'M' :#ToutTerrJ1
            if Joueur == 1:
                Cible = self.zones["J1Main"]
            else :
                Cible = self.zones["J2Main"]

        elif Step == 'm':#ToutTerrJ2
            if Joueur == 1:
                Cible = self.zones["J2Main"]
            else :
                Cible = self.zones["J1Main"]

        return Cible
            #-Cible (Carte.s)
            #   -Biblio             =
            #   -Selection          #
            #   -Rand               ?
            #   -ToutProc           P
            #   -ToutDef            D
            #   -ToutTerrJ1 J2      T t

    def GetDest(self, Step):
        if Step[2] == '=':#Biblio
            pass

        elif Step[2] == '?':#Rand
            pass

        elif Step[2] == 'P':#Proc
            pass

        elif Step[2] == 'D':#Def
            pass

        elif Step[2] == 'T' :#TerrJ1
            pass

        elif Step[2] == 't':#TerrJ2
            pass

        elif Step[2] == 'M' :#TerrJ1
            pass

        elif Step[2] == 'm':#TerrJ2
            pass

    #Execute la séquence
    def ExecuteSeq(self, Fonction):

        Executable = True
        if Fonction != "":
            Steps = Fonction.split("-")

            #Cible Action Destination
            Joueur = self.joueur
            if self.joueur == 1:
                AutreJoueur = 2
            else:
                AutreJoueur = 1

            for Step in Steps:

                Cible = GetCible(Step[0])

                if Cible != 0:

                    if Step[1] == '@':#Déplace

                        Dest = self.GetDest(Step[2])
                        # Bouger Carte
                        return True

                    elif Step[1] == '+' or Step[1] == '-':#Marqueur
                        #Ajout Marqueur
                        return True

                else:
                    return False
        else : 
            return True
    #Remet à Zero des séquences
    def Reset(self):
        self.target = 0
        for f in self.fonctions:
            f["State"] = 0
    
    def Ciblage(self):
        if self.target == 0:
            if Select:
                pass
            elif Rand:
                self.target = random.choice(self.zones[random.choice(list(self.zones.keys()))])
            elif All:
                self.target = self.zones["Proc"].cartes
        else:
            pass
            
        
