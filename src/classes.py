from random import randint, shuffle
import os
import time
import json
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
    def __repr__(self) -> str:
        return self.__str__()
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
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        """Deck -> str
        Renvoie une chaine de caractère décrivant le deck. """
        return ", ".join(map(str, self.contenu)) if self.contenu else "Deck vide."
    

    
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
        self.main = [carte1, carte2, *self.main]
    
    def ramasser_all(self, *cartes):
        self.main = [*cartes, *self.main]
    

class Bataille():
    def __init__(self, j1, j2) -> None:
        self.joueur1:Joueur = j1
        self.joueur2:Joueur = j2
        self.pile = []

        self.deck = Deck()
        self.deck.melanger()
        self.distribuer()


    def fin_partie(self, ind:int=0, getPlayer:bool = False) -> bool|Joueur:
        """ Bataille, int -> bool
        Vérifie si la partie est terminée. Si ind est passé,alors on vérifie si un des deux joueurs a ind cartes, sinon 0. """
        print("Fin de partie: ", len(self.joueur1.main) == ind or len(self.joueur2.main) == ind)
        checkFP = len(self.joueur1.main) == ind or len(self.joueur2.main) == ind
        if getPlayer:
            return self.joueur1 if len(self.joueur1.main) > len(self.joueur2.main) else self.joueur2
        return checkFP

    def jouer_tour(self, skipcheck = False) -> None:
        if self.fin_partie():
            if len(self.pile) > 0:
                self.fin_partie(getPlayer=True).ramasser_all(*self.pile)
                self.pile = []
            return # Partie finie, même en cas de bataille !
                
        print("On commence un tour avec {}, {}".format(self.joueur1.main[-1], self.joueur2.main[-1]))
        # On compare les deux cartes
        print(len(self.joueur1.main), len(self.joueur2.main))
        self.pile.append(self.joueur1.jouer_carte())
        self.pile.append(self.joueur2.jouer_carte())
        print(len(self.joueur1.main), len(self.joueur2.main))
        print(len(self.pile))

        carte_une_bat_deux = self.pile[-2].bat(self.pile[-1])
        if skipcheck: return carte_une_bat_deux
        # Si la carte une est égale à la carte deux, la fonction renvoie None. Donc, bataille.
        if carte_une_bat_deux is None:
            return self.bataille()

        if carte_une_bat_deux:
            print("Le joueur 1 gagne !")
            self.joueur1.ramasser_all(*self.pile)
            print(self.joueur1.main)
            self.pile = []
        else:
            print("Le joueur 2 gagne !")
            self.joueur2.ramasser_all(*self.pile)
            print(self.joueur2.main)
            self.pile = []

# ToDo: ajouter un check pour vérifier si bataille à la fin + plus de cartes ne fait plus crash.
# En cas de bataille, choisir entre réinjecter une carte random ou conclure sur la personne ayant le
# plus de points


    def bataille(self):
        # Dans le cadre de la bataille:
        self.jouer_tour(True)
        self.jouer_tour()

    def distribuer(self) -> None:
        """ Bataille -> NoneType
        Distribue le deck aux joueurs """
        print("Mon deck est ", self.deck)
        for i in range(0, len(self.deck)):
            if i % 2 == 0:
                self.joueur1.piocher_carte(self.deck)
            else:
                self.joueur2.piocher_carte(self.deck)
        # Tests de la partie bataille
        # self.joueur1.main.append(Carte("trèfle", 5))
        # self.joueur2.main.append(Carte("trèfle", 5))
        print("Deck du joueur 1: ", self.joueur1.main)
        print("Deck du joueur 2: ", self.joueur2.main)

    def load_deck(self, copied_deck:dict) -> bool:
        """Bataille, dict -> bool
        Charge la configuration du deck (copied_deck).
        Renvoie True or False si la fonction se termine correctement.
        """
        if not copied_deck:
            return False
        cartes_j1 = copied_deck.get("joueur1")
        cartes_j2 = copied_deck.get("joueur2")

        self.joueur1.main = []
        self.joueur2.main = []
        for carte in cartes_j1:
            self.joueur1.main.append(Carte(carte.get("couleur"), carte.get("nombre")))

        for carte in cartes_j2:
            self.joueur2.main.append(Carte(carte.get("couleur"), carte.get("nombre")))
        if len(self.joueur1.main) + len(self.joueur2.main) == 52:
            return True
        return Exception("Deck chargé Invalide. La somme des cartes des deux joueurs doit être égale à 52.")
    
    def save_deck(self) -> "Bataille":
        """ Bataille -> Bataille
        Sauvegarde le deck actuel. """
        deck =  {
            "joueur1": [{"couleur": carte.couleur, "nombre": carte.nombre} for carte in self.joueur1.main],
            "joueur2": [{"couleur": carte.couleur, "nombre": carte.nombre} for carte in self.joueur2.main]
        }

        with open(f"{time.time()}-deck.json", "w", encoding="utf-8") as f:
            json.dump(deck, f, ensure_ascii=False, indent=4)
        return self

    def run(self) -> Joueur | None:
        """ Bataille -> Joueur | NoneType
        Lance une partie de bataille """
        cround = 0
        while not self.fin_partie():
            if cround <= 2000:
                self.jouer_tour()
                # input("Prochain tour\n")
                print(f"CARTES JOUEUR 1 [{len(self.joueur1.main)}]", ": ", self.joueur1.main)
                print(f"CARTES JOUEUR 2 [{len(self.joueur2.main)}]: ", self.joueur2.main)
                cround += 1
            else:
                print("Trop de tours, on arrête.")
                break
        print("La partie est finie !")
        joueur = self.fin_partie(getPlayer=True)
        print("Le joueur gagnant est: ", joueur, "avec ", len(joueur.main), "cartes.")
        return joueur