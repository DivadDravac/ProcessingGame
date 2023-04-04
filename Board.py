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
        self.Defausse = Zone.Defausse()
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
        self.Tour = 1
        self.step = 0

        for PiocheInit in range(0,NbPiocheInit):
            self.Bibliotheque.Piocher(self.Joueur1, True)
            self.Bibliotheque.Piocher(self.Joueur2, True)
        
        self.BoucleTour(0)

    def BoucleTour(self, Carte):
        TourJoueur = 0
        TourPasJoueur = 0

        if self.Tour == 1:
            TourJoueur = self.Joueur1
            TourPasJoueur = self.Joueur2
        else:
            TourJoueur = self.Joueur2
            TourPasJoueur = self.Joueur1
        print("Debut de tour")
        if self.ExecuteEtape(0,"Debut",Carte, TourJoueur, TourPasJoueur):#Debut Tour
            print("Pioche")
            if self.ExecuteEtape(1,"Pioche",Carte, TourJoueur, TourPasJoueur):#Pioche
                print("Joue")
                if self.ExecuteEtape(2,"Joue",Carte, TourJoueur, TourPasJoueur):#Joue
                    print("Execute")
                    if self.ExecuteEtape(3,"Execute",Carte, TourJoueur, TourPasJoueur):#Execute
                        print("Fin")
                        if self.ExecuteEtape(4,"Fin",Carte, TourJoueur, TourPasJoueur):#Fin
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

    def ExecuteEtape(self, EtapeNb, Etape, Carte, TourJoueur, TourPasJoueur):
        if self.step == EtapeNb:
            if EtapeNb == 0 :# Etape de début de tour
                if self.CheckExeptions(Etape, Carte):#check etape de début
                    self.step = EtapeNb+1
                    TourJoueur.Terr.ResetZone()
                    TourPasJoueur.Terr.ResetZone()

            if EtapeNb == 1 :#Etape de pioche

                ret = self.Bibliotheque.Piocher(Joueur)#Tcheck pioche
                if ret != False and ret != -1:#Si pioche
                        self.step = EtapeNb+1
                        TourJoueur.Terr.ResetZone()
                        TourPasJoueur.Terr.ResetZone()
                elif ret == False:#Si plus de pioche
                    print("Joueur " + str(self.Tour) + "a perdu.")

            elif EtapeNb == 2 :#CarteJouée
                if TourJoueur.JoueCarte(Carte, TourPasJoueur):
                    self.step = EtapeNb+1
                    TourJoueur.Terr.ResetZone()
                    TourPasJoueur.Terr.ResetZone()

            elif EtapeNb == 3:#Execution
                if self.Proc.ExecuterFonctions("Execute", Carte):
                    self.step = EtapeNb+1
                    TourJoueur.Terr.ResetZone()
                    TourPasJoueur.Terr.ResetZone()


            elif EtapeNb == 4:#Fin de tour
                if self.CheckExeptions(Etape, Carte):
                    if self.Tour == 1:
                        self.Tour = 2
                    else:
                        self.Tour = 1
                    self.step = 0#retour à l'étape 1

                    TourJoueur.Terr.ResetZone()
                    TourPasJoueur.Terr.ResetZone()

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
