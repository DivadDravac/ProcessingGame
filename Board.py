import Carte
import LoaderCartes
import Joueur
import Zone

class Board:
    def __init__(self, NomBiblio = "", NbPiocheInit = 3):
        
        #Init des Zones
        self.Bibliotheque = Zone.Bibliotheque()
        self.Joueur1 = Joueur.Joueur(1,"nom")
        self.Joueur2 = Joueur.Joueur(2,"nom")
        self.Defausse = Zone.Defausse([self.Joueur1.Terr, self.Joueur2.Terr])
        self.Proc = Zone.Processeur()

        Zones = {"Biblio"   :self.Bibliotheque,
                "Defausse"      :self.Defausse,
                "Proc"          :self.Proc,
                "J1Main"        :self.Joueur1.Main,
                "J1Terr"        :self.Joueur1.Terr,
                "J2Main"        :self.Joueur2.Main,
                "J2Terr"        :self.Joueur2.Terr}

        #Init des Cartes
        Cartes = LoaderCartes.Chargeur(Zones).Init(NomBiblio)
        self.Bibliotheque.SetBibliotheque(Cartes)


        #Alloc des cartes
        self.Tour = [self.Joueur1.Terr, self.Joueur2.Terr]
        self.step = 0

        for PiocheInit in range(0,NbPiocheInit):
            self.Bibliotheque.Piocher(self.Joueur1, True)
            self.Bibliotheque.Piocher(self.Joueur2, True)
        
        self.BoucleTour(0)

    def BoucleTour(self, Carte):

        print("Debut de tour")
        if self.ExecuteEtape(0,"Debut",Carte):#Debut Tour
            print("Pioche")
            if self.ExecuteEtape(1,"Pioche",Carte):#Pioche
                print("Joue")
                if self.ExecuteEtape(2,"Joue",Carte):#Joue
                    print("Execute")
                    if self.ExecuteEtape(3,"Execute",Carte):#Execute
                        print("Fin")
                        if self.ExecuteEtape(4,"Fin",Carte):#Fin
                            self.BoucleTour(0)
                
    def CheckExeptions(Etape, Carte):
        if TourJoueur.Terr.ExecuterFonctions(Etape, Carte) :
            if TourPasJoueur.Terr.ExecuterFonctions(Etape, Carte):
                return True

            else:#Demande de cible autre joueur
                print("Problème Cible Joueur")
                return False
                
        else:#Demande de cible autre joueur
            print("Problème Cible Antijoueur")
            return False

    def ExecuteEtape(self, EtapeNb, Etape, Carte):
        reset = False

        if self.step == EtapeNb:
            if EtapeNb == 0 :# Etape de début de tour
                if self.CheckExeptions(Etape, Carte):#check etape de début
                    self.step = EtapeNb+1
                    reset = True


            if EtapeNb == 1 :#Etape de pioche

                ret = self.Bibliotheque.Piocher(Joueur)#Tcheck pioche
                if ret != False and ret != -1:#Si pioche
                        self.step = EtapeNb+1
                        reset = True

                elif ret == False:#Si plus de pioche
                    print("Joueur " + self.Tour[0].Nom + "a perdu.")

            elif EtapeNb == 2 :#CarteJouée
                if self.Tour[0].JoueCarte(Carte, TourPasJoueur):
                    self.step = EtapeNb+1
                    reset = True


            elif EtapeNb == 3:#Execution
                if self.Proc.ExecuterFonctions("Execute", Carte):
                    self.step = EtapeNb+1
                    reset = True

            elif EtapeNb == 4:#Fin de tour
                if self.CheckExeptions(Etape, Carte):
                    Buff = self.Tour[0]
                    self.Tour[0] = self.Tour[1]
                    self.Tour[1] = Buff

                    self.step = 0 #retour à l'étape 1

            if reset:
                self.Tour[0].Terr.ResetZone()
                self.Tour[1].Terr.ResetZone()

            print("Etape OK")
            
            return True
                

                    
            
        else:#Etape dépassée
            if self.step > EtapeNb:
                print("Etape passée")
                return True
                
            else:#Etape futur
                print("Etape future")
                return False
                
                    


    def SelectionneCarte(self, Carte):

        self.BoucleTour(Carte)
