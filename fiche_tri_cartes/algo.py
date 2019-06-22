#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:17:43 2019

"""

from random import randrange,shuffle
from cartes import *

print("Jeu avec 2 couleurs")
jeu = cartes(20,2)
print(jeu.main)
print("Tri 2C (2 couleurs) - ne modifie pas la main")
print(jeu.tri2C()) # ne modifie pas la main
print("Tri 2A (2 couleurs)")
print(jeu.tri2A())
print("mélange du jeu de carte")
jeu.melanger()
print(jeu.main)
print("Tri 2B (2 couleurs)")
print(jeu.tri2B())

print("Jeu avec 4 couleurs")
jeu4 = cartes(32,4)
print(jeu4.main)
print("Tri B avec 4 couleurs")
print(jeu4.triB())

print("jeu non equi")
jeuF = cartes(32,4,equi=False)
print(jeuF.main)
print("Tri B avec 4 couleurs (cas non equi)")
print(jeuF.triB())


import timeit
test1 = timeit.Timer("jeu = cartes.cartes(1000,2);jeu.tri2A()", "import cartes;")
print("TRI A",test1.timeit(1000))
test2 = timeit.Timer("jeu = cartes.cartes(1000,2);jeu.tri2B()", "import cartes;")
print("TRI B",test2.timeit(1000))
test3 = timeit.Timer("jeu = cartes.cartes(1000,2);jeu.tri2C()", "import cartes;")
print("TRI C",test3.timeit(1000))

