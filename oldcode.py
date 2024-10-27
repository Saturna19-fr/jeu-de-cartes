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