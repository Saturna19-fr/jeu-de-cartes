# Code de Thibault
from classes import *
from json import load

bataille1 = Bataille(Joueur(), Joueur())
# bataille1.load_deck(load(open("valid_deck.json", "r", encoding="utf-8")))
bataille1.run()