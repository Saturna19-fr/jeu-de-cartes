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
        deck = json.load(open("valid_deck.json"))
        print(bataille.load_deck(deck))

        run = bataille.run()
        self.assertEqual(run, j1)
        self.assertEqual(len(j1.main), 52)
        self.assertEqual(len(j2.main), 0)
        self.assertTrue(bataille.fin_partie())


if __name__ == "__main__":
    unittest.main()