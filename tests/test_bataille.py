# Code de Thibault
import unittest
import src.classes
import json

class Test_TestBataille(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_partie_valide(self):
        j1 = src.classes.Joueur()
        j2 = src.classes.Joueur()

        bataille = src.classes.Bataille(j1, j2)
        deck = json.load(open("valid_deck.json", encoding="utf-8"))
        print(bataille.load_deck(deck))

        run = bataille.run()
        self.assertEqual(run, j1)
        self.assertEqual(len(j1.main), 52)
        self.assertEqual(len(j2.main), 0)
        self.assertTrue(bataille.fin_partie())

    def test_partie_minime(self):
        carte_constructor = src.classes.Carte
        bataille = src.classes.Bataille(
            src.classes.Joueur(id = 1),
            src.classes.Joueur(id = 2),
            CustomDeck=src.classes.Deck(
                predef_content=[
                    carte_constructor("carreaux", 5),
                    carte_constructor("trèfle", 12),
                    carte_constructor("pic", 9),
                    carte_constructor("coeur", 7),
                    carte_constructor("pic", 7),
                    carte_constructor("trèfle", 9),
                    carte_constructor("trèfle", 8),
                    carte_constructor("trèfle", 3),
                    ]
            )
        )
        winner = bataille.run()
        print(winner._hiddenid ,"a gagné !")

if __name__ == "__main__":
    unittest.main()