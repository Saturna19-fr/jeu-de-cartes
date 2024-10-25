import unittest
import src.classes
class Test_TestIsValid(unittest.TestCase):
    def setUp(self):
        self.carte = src.classes.Carte("trèfle", 8)
    
    def test_affiche_correctement(self):
        self.assertEqual(str(self.carte), "8 de trèfle")

    def test_bat_correctement(self):
        carte_test = src.classes.Carte("trèfle", 5)
        carte_test2 = src.classes.Carte("pic", 12)
        carte_test3 = src.classes.Carte("carreau", 14)

        self.assertTrue(self.carte.bat(carte_test), "Le 8 doit battre le 5")
        self.assertFalse(self.carte.bat(carte_test2), "Le 12 doit battre le 8")
        self.assertFalse(self.carte.bat(carte_test3), "Le 14 doit battre le 8")

if __name__ == "__main__":
    unittest.main()