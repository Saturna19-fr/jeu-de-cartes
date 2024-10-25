from random import randint, shuffle

CARTES = {
    14: "As",
    13: "Dame",
    12: "Roi",
    11: "Valet",
    10: "10",
    9: "9",
    8: "8",
    7: "7",
    6: "6",
    5: "5",
    4: "4",
    3: "3",
    2: "2"
}


class Carte:
    """Représente une carte d'un jeu"""

    def __init__(self, couleur:str, nombre:int) -> None:
        self.couleur = couleur
        self.nombre = nombre

    def __str__(self) -> str:
        """ Carte -> str
        Méthode spéciale. Permet d'afficher la carte. """
        return "{nb} de {col}".format(nb = CARTES[self.nombre], col = self.couleur)
    
    ## TEST: bat avec plusieurs cartes
    def bat(self, other: "Carte") -> bool | None:
        """ Carte, Carte -> bool | NoneType
        Compare deux cartes. Renvoie True si self bat other, False sinon. """
        if other.nombre != self.nombre:
            return self.nombre > other.nombre
        # Ca fonctionne parce que une fonction retourne None par défault.

class Deck:
    """Représente un paquet de 52 cartes"""
    def __init__(self) -> None:
        self.contenu = []
        for valeur in ["trèfle", "pic", "carreaux", "coeur"]:
            for nb in CARTES.keys():
                self.contenu.append(Carte(valeur, nb))
    
    # def tirer(self, indice:int = 0) -> Carte:
    def tirer(self, preindice:int = None) -> Carte:
        """Deck -> Carte
        Tire une carte du deck"""
        indice = preindice or randint(0, len(self.contenu)-1)
        carte:Carte = self.contenu[indice]
        self.contenu.pop(indice)
        return carte
    
    def melanger(self) -> None:
        """Deck -> NoneType
        Mélange le deck. """
        shuffle(self.contenu)

    def __len__(self) -> int:
        """Deck -> int
        Renvoie la taille du deck. """
        return len(self.contenu)
    
    def __sizeof__(self) -> int: return self.__len__()

    def __str__(self) -> str:
        """Deck -> str
        Renvoie une chaine de caractère décrivant le deck. """
        return ", ".join(map(str, self.contenu))
    

    
class Joueur:
    """Représente un joueur"""
    def __init__(self) -> None:
        self.main = []


    def piocher_carte(self, deck:Deck) -> None:
        """Joueur, Deck -> NoneType
        Le joueur tire une carte du deck et l'ajoute à sa main"""
        carte = deck.tirer()
        if not carte:
            return print("Il n'y a plus de cartes !")
        self.main.append(carte)

    def jouer_carte(self) -> Carte:
        """Joueur -> Carte
        Joue une carte de la main (celle au sommet)."""
        carte = self.main[-1]
        self.main.pop()

    def ramasser(self, carte1:Carte, carte2:Carte) -> None:
        """ Joueur, Carte, Carte -> Nonetype
            Ajoute les deux cartes en dessous de la main. """
        return [carte1, carte2, *self.main]
    

class Bataille:
    """Simule le jeu de la bataille entre deux joueurs"""
    def __init__(self, j1, j2):
        """Bataille, Joueur, Joueur -> NoneType"""
        pass

    def distribuer(self):
        """ Bataille -> NoneType
        Distribue le deck aux joueurs """
        pass

    def jouer_tour(self):
        """ Bataille -> NoneType
        Simule un tour de bataille """
        pass

    def fin_partie(self, joueur):
        """ Bataille, Joueur -> Joueur
        Vérifie si la partie est terminée. Si c'est le cas, renvoie le joueur gagnant. """
        pass

    def bataille(self):
        """ Bataille -> NoneType
        Déclenche une bataille """
        pass

    def run(self):
        """ Bataille -> Joueur
        Simule une bataille entre les deux joueurs """
        pass