#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:23:25 2019

@author: Les 3P
"""
import numpy as np
from math import sqrt
from PIL import Image
from sklearn.datasets import fetch_openml


def distance(a,b):
    '''
    @parameter: liste de même dimension 784 - correspond au jeu mnist
    @return:    la distance entre deux points (int)
    @attention: ne vérifie pas la dimension des listes
    '''
    return sqrt(sum([(a[i]-b[i])**2 for i in range(784)]))

def lePlusProcheVoisin (image,data):
    '''
    @parameter: image est une liste représentant l'image 
    @var :      data est liste d'image de référence
    @return:    renvoi l'indice du tableau data dont la distance entre image et cet élément est minimal
    '''
    lePlusPres = 0
    distanceMin = float("inf")
    for i in range(len(data)):
        di = distance (image, data[i])
        if di != 0 and di < distanceMin:
            lePlusPres = i
            distanceMin = di
    return (lePlusPres)

def lesKplusProchesVoisins (image, k, data):
    '''
    @summary:   détermine une liste des indices du tableau data dont la distance entre image et ces éléments est minimal
    @parameter: image est une liste représentant l'image
                k est le nombre de voisins à chercher
    @var :      data est liste d'image de référence
    @return:    liste
    '''
    listeDesDistances = []
    for img in data:
        listeDesDistances.append (distance (image, img))
    Kppv = []
    for i in range (k):
        p = float ("inf")
        for j in range (len (data)):
            if listeDesDistances [j] != 0 and listeDesDistances [j] < p and j not in Kppv:
                p = listeDesDistances [j]
                indice = j
        Kppv. append (indice)
    return (Kppv)

def lesKplusProchesVoisins2 (image, k, data):
    '''
    @summary:   détermine une liste des indices du tableau data dont la distance entre image et ces éléments est minimal
    @parameter: image est une liste représentant l'image
                k est le nombre de voisins à chercher
    @var :      data est liste d'image de référence
    @return:    liste
    '''
    listeDesDistances = []
    for img in data:
        listeDesDistances.append (distance (image, img))
    Kppv = []
    for i in range (k):
        p = float ("inf")
        for j in range (len (data)):
            if listeDesDistances [j] != 0 and listeDesDistances [j] < p and j not in Kppv:
                p = listeDesDistances [j]
                indice = j
        Kppv. append (indice)
    return (Kppv)

def predire (l,k,data):
    '''
    @return : int
    '''
    Kppv = lesKplusProchesVoisins(l,k,data)
    decomptes = {'0':1, '1':0, '2':0 , '3':0, '4':0, '5':1, '6':0, '7':0 , '8':0, '9':0}
    for indice in Kppv:
        decomptes[target[indice]] += 1
    plusGrandDecompte = decomptes['0']
    for i in '0123456789':
        if decomptes [i] > plusGrandDecompte:
                plusGrandDecompte = decomptes [i]
                indice = i
    return indice

mnist = fetch_openml('mnist_784',cache=True, version = 1, data_home = '/home/pascal/Dropbox/cours/NSI/projet_bloc1/')

sample = np.random.randint(70000, size=5000)
data = mnist.data[sample]
target = mnist.target[sample]

ecrit = Image.open("ecrit2.pgm")
# met l'image dans un tableau qui est de dimension 784
img =list(ecrit.getdata())
img = [255-i for i in img]

#indice = lePlusProcheVoisin(img,data)
#print(img)
#print(target[indice])
print(predire(img,6,data))