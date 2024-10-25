import unittest
from classes import Carte

class TestCartes(unittest.TestCase):

    # Création de cartes
    def setup(self):
        self.carte = Carte("trèfle", 8)
    
    def affiche_correctement(self):
        self.assertIs(str(self.carte), "8 de trèfle")

    def bat_correctement(self):
        carte_test = Carte("trèfle", 5)
        carte_test2 = Carte("pic", 12)
        carte_test3 = Carte("carreau", 14)

        self.assertTrue(self.carte.bat(carte_test), "Le 8 doit battre le 5")
        self.assertFalse(self.carte.bat(carte_test2), "Le 12 doit battre le 8")
        self.assertFalse(self.carte.bat(carte_test3), "Le 14 doit battre le 8")


if __name__ == '__main__':
    unittest.main()