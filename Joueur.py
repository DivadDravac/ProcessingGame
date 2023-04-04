import Zone


class Joueur:
    def __init__(self,joueur , nom="Defaut"):
        self.Nom = nom
        self.Joueur = joueur
        self.Main = Zone.Main(joueur)
        self.Terr = Zone.Terrain()
        self.Proc = Zone.Processeur()

    def JoueCarte(self, Carte, AutreJoueur):
        if Carte in self.Main.cartes:#Joue une carte
            if Carte.ExecuterFonction("Joue"):
                self.Proc.Move(Carte, self.Main)    
                self.Main.UpdateMain()
        else:
            #selectionne une carte
            pass

            