import Zone


class Joueur:
    def __init__(self,joueur , nom="Defaut"):
        self.Nom = nom
        self.Joueur = joueur
        self.Main = Zone.Main(joueur)
        self.Terr = Zone.Terrain()

    def JoueCarte(self, Carte):
        if Carte in self.Main.cartes:
              self.Main.cartes.remove(Carte)          
        self.Main.UpdateMain()