#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Pascal,Patrick
"""

from random import randrange,shuffle

class cartes:
    """
        modélisation d'un jeu de cartes
    """
    def __init__(self,n,couleurs = 2, equi = True):
        self.couleurs=couleurs
        self.taille = n
        if equi == True:
            p = self.taille//couleurs
            r = n - p*couleurs # si la taille n'est pas un multiple de la couleur
            self.main = [i for j in range(p) for i in range(couleurs)]
            if r !=0:
                for i in range(r):
                    self.main.append(couleurs-1)
            shuffle(self.main) # on mélange le paquet
        else:
            self.main = [randrange(0,couleurs) for i in range(self.taille)]

    def melanger(self):
        shuffle(self.main)

    def tri2A(self):
        """
        Tri des couleurs avec une seule liste en mémoire à la manière du 
        drapeau hollandais
        Seulement deux couleurs
        """
        pr = self.taille # indice à partir duquel on est sûr d'avoir des rouges
        # on l'initialise au successeur du dernier terme
        pa = 0
        while pa < pr:
            if self.main[pa] == 0: # on fait le choix que 0 représente la couleur noire
                pa += 1
            else:
                pr -= 1
                self.main[pa], self.main[pr] = self.main[pr], self.main[pa]
        return self.main

    def tri2B(self):
        """
        Tri des couleurs avec une seule liste en mémoire
        mais on ne retourne que la carte du dessus
        Seulement deux couleurs
        """
        pn = self.taille-1 # indice à partir duquel on range les noires

        for i in range(self.taille):
            c=self.main[0] # la première carte
            if c == 0: # on fait le choix que 0 représente la couleur noire
                # insertion de la carte à sa place
                self.main = self.main[1:pn+1]+[c]+self.main[pn+1:] 
            else: # la carte est rouge
                self.main =self.main[1:]+[c] # on la met à la fin
            pn -= 1 # l’indice diminue
        return self.main

    def triB(self):
        """
        Tri des couleurs avec une seule liste en mémoire en insérant les couleurs au bon endroit,
        Nombre de couleurs quelconque
        """
        lp=[self.taille-1 for i in range(self.couleurs)]
        # indices des indices où insérer les cartes pour chaque espace de couleur
        for i in range(self.taille):
            c=self.main[0] # la première carte
            # insertion de la carte à sa place
            self.main = self.main[1:lp[c]+1]+[c]+self.main[lp[c]+1:] 
            for p in range(c+1):
                lp[p]-=1 # Les indices des couleurs inférieures diminuent
        return self.main

    def tri2C(self):
        """
        Tri des couleurs avec la construction d'une nouvelle liste
        Seulement 2 couleurs
        """
        nv = []
        nv.append(self.main[0])
        for pa in range(1,self.taille):
            if self.main[pa] == 0:
                nv.insert(0, self.main[pa])
            else:
                nv.append(self.main[pa])
        return nv

