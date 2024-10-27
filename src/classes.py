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
        return carte

    def ramasser(self, carte1:Carte, carte2:Carte) -> None:
        """ Joueur, Carte, Carte -> Nonetype
            Ajoute les deux cartes en dessous de la main. """
        return [carte1, carte2, *self.main]
    

class Bataille:
    """Simule le jeu de la bataille entre deux joueurs"""
    def __init__(self, j1, j2):
        """Bataille, Joueur, Joueur -> NoneType"""
        self.joueur1:Joueur = j1
        self.joueur2:Joueur = j2
        self.pile = [] # Ca sera toujours 2 cartes, la première est celle du joueur 1, la deuxième celle du joueur 2.
        self.deck = Deck()
        self.deck.melanger() 


    def distribuer(self):
        """ Bataille -> NoneType
        Distribue le deck aux joueurs """
        for i in range(0, len(self.deck)):
            if i % 2 == 0:
                self.joueur1.piocher_carte(self.deck)
            else:
                self.joueur2.piocher_carte(self.deck)
        print(self.deck)

    def jouer_tour(self, forceClaim:bool = False) -> Joueur | None:
        """ Bataille, bool -> Joueur | NoneType
        Simule un tour de bataille """
        print("Nouveau tour...")
        if self.fin_partie(self.joueur1):
            return self.joueur2
        if self.fin_partie(self.joueur2):
            return self.joueur1
        self.pile.append(self.joueur1.jouer_carte())
        self.pile.append(self.joueur2.jouer_carte())
        print(self.pile)
        # On compare les deux cartes
        
        if len(self.pile) == 2 or forceClaim:
            bat = self.pile[-2].bat(self.pile[-1])
            print(self.pile)
            if bat is None:
                return self.bataille()
            if bat:
                print("Le joueur 1 gagne !")
                self.joueur1.ramasser(*self.pile)
            else:
                print("Le joueur 2 gagne !")
                self.joueur2.ramasser(*self.pile)
            self.pile = []


    def fin_partie(self, joueur = None):
        """ Bataille, Joueur -> Joueur
        Vérifie si la partie est terminée. Si c'est le cas, renvoie le joueur gagnant. """
        if joueur:
            return len(joueur.main) == 0
        return len(self.joueur1.main) == 0 or len(self.joueur2.main) == 0

    def bataille(self):
        """ Bataille -> NoneType
        Déclenche une bataille """
        self.jouer_tour() # Juste append, vu qu'il y a déjà deux cartes.
        winner = self.jouer_tour(forceClaim=True) # On joue une carte de plus pour déterminer le gagnant; on force la comparaison.
        print(f"Bataille remportée par {winner}")

    def run(self):
        """ Bataille -> Joueur
        Simule une bataille entre les deux joueurs """
        self.distribuer()
        while True:
            if self.fin_partie():
                break
            self.jouer_tour()
            
        print("Partie terminée !")