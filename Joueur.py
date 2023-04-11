import Zone


class Joueur:
    def __init__(self ,Numero, nom="Defaut"):
        self.Nom = nom
        self.numero = Numero
        self.Main = Zone.Main(self)
        self.Terr = Zone.Terrain()
        self.Proc = Zone.Processeur()

    def JoueCarte(self, Carte, AutreJoueur):
        if Carte in self.Main.cartes:#Joue une carte
            if Carte.ExecuterFonction("Joue",Carte):
                self.Proc.Move(Carte, self.Main)    
                self.Main.UpdateMain()
                return True
        else:
            #selectionne une carte
            pass

            