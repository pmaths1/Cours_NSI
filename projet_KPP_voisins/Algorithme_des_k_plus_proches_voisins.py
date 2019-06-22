#!/usr/bin/env python
# coding: utf-8

# # Algorithme des *k* plus proches voisins
# Le lien vers [openclassroom](https://openclassrooms.com/fr/courses/4011851-initiez-vous-au-machine-learning/4022441-tp-entrainez-le-modele-des-k-plus-proches-voisins-k-nn)
# 
# Celui vers le [TP de l'université de Lille donné dans moodle](http://www.grappa.univ-lille3.fr/~ppreux/ensg/miashs/l3-ap/tps/kppv/)
# 
# L'objectif de ce TP est de faire reconnaître automatiquement par l'ordinateur des chiffres manuscrits (pour lire des chèques, lire des codes postaux par exemple). ![enveloppe](lettres.jpg)

# ## 1. Lecture du jeux d'exemples
# 
# Avant même d'implanter l'algorithme des *k* plus proches voisins, nous avons besoin d'exemples qui seront traités par l'algorithme. Aussi, commençons par lire un jeu de données.
# 
# Il s'agit d'un jeu de données très célèbre appelé MNIST. Il est constitué d'un ensemble de 70000 images, 28x28 pixels, en noir et blanc annoté du chiffre correspondant (entre 0 et 9). Ce jeu utilise des données réelles qui ont déjà été pré-traitées pour être plus facilement utilisables par un algorithme.
# 
# ![Un extrait du type d'images que l'on trouve dans le dataset MNIST](extrait_MNIST.png)
# 
# Le jeu de données est relativement petit mais pour l'algorithme des *k* plus proches voisins, il est déjà trop gros pour obtenir rapidement des résultats. On va donc effectuer un échantillonnage et travailler sur seulement 5000 données.

# ## 2. Déterminer le plus proche voisin d'un point
# ### 2.1Distance entre deux images

# 
# 
# Pour évaluer la différence entre deux images, on va définir une distance entre deux images. Les images sont des images [PGM](https://fr.wikipedia.org/wiki/Portable_pixmap#Fichier_binaire_2), c'est à dire en niveau de gris.
# 
# * Pour tous les pixels de l'image on calcule la différence des valeurs d'intensité, dont on supprime le signe (abs)
# * On somme toutes ces différences
# 
# ![comparaison](distance_eleve.png)
# 
# 1. Pour les deux images précédentes, déterminez la distance.
# 2. Écrire une fonction qui calcule la distance entre deux images. Une image sera représentée comme une liste des valeurs de gris des pixels

# In[ ]:


def distance (a, b):
    somme = 0
    for i in range (784):
        somme += abs(a[i] - b [i]) 
    return somme

#def distance(a,b):
#    return sum([abs(a[i]-b[i]) for i in range(784)])


# ### 2.2 Exemple d'utilisation
# 
# Nous allons calculer la distance entre quelques chiffres manuscrits.
# 
# |image1|image2|image3|
# |------|------|-----|
# |![chiffre5](ecrit1.png)|![chiffre5](ecrit2.png)|![chiffre5](ecrit3.png)|
# 
# On cherche à comparer la première image aux deux suivantes. Bien que nous voyons tout de suite le résultat, déterminer les distances.
# 
# **Librairie PIL:**
# * ouvrir une image `Image.open(nom du fichier)`
# * Récuperer les valeurs des pixels de notre image `monimage.getdata()`, il faut la transformer en liste avec la commande `list(...)`
# 

# In[ ]:


from PIL import Image
from IPython.display import display

ecrit1 = Image.open("ecrit1.pgm")
# met l'image dans un tableau qui est de dimension 784
img1 =list(ecrit1.getdata())

ecrit2 = Image.open("ecrit2.pgm")
# met l'image dans un tableau qui est de dimension 784
img2 =list(ecrit2.getdata())

ecrit3 = Image.open("ecrit3.pgm")
# met l'image dans un tableau qui est de dimension 784
img3 =list(ecrit3.getdata())

d12 = distance(img1,img2)
d13 = distance(img1,img3)

if d13<d12:
    print("image 1 est plus proche de l'image de 3 que de l'image 2")
else:
    print("image 1 est plus proche de l'image de 2 que de l'image 3")
display(ecrit1)


# ## 3. Parcours le jeu de données

# Le jeu de données est relativement petit mais pour l'algorithme des k plus proches voisins, il est déjà trop gros pour obtenir rapidement des résultats. On va donc effectuer un échantillonnage et travailler sur seulement 5000 données.
# 
# On obtient deux listes, **data** et **target**.
# * data contient les images sous forme d'une liste 28*28 = 784 entiers compris entre 0 et 255 correspondant aux différentes nuances de gris (255 étant blanc et 0 noir)
# * target contient les chiffres correspondant à l'image</li>
# 

# In[ ]:

# Télécharger les données mnist c'est un peu long
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1,data_home='/home/pascal')

#print(mnist.data.shape)

#print(mnist.target.shape)


# In[ ]:


import numpy as np

sample = np.random.randint(70000, size=5000)

data = mnist.data[sample]
#data = map(lambda x: map(int,x),data)

target = mnist.target[sample]
#target = map(int,target)


# Afficher la liste correspondant à la 23ème image du jeu de données. A quel chiffre corrrespond cette image ?

# In[ ]:


print (data[23],'\n')

print ('Le chiffre represente est :', target[23])


# Dans la cellule ci-dessous vous allez prendre deux élèments de notre jeu de données, calculer la distance entre ces deux images et indiquer le chiffre qu'il représente

# In[77]:


image1 = data[23]
image2 = data[65]
distance(image1,image2)
target[23]


# ## 4. Déterminer les *k* plus proches voisins d'un point

# ### 4.1 Le plus proche voisin avec le jeu de données

# Écrire une fonction lePlusProcheVoisin qui prend en paramètre une image (une liste de 784 entiers compris entre 0 et 255) et renvoie l'indice dans data du plus proche voisin.

# In[75]:


def lePlusProcheVoisin (image):
    lePlusPres = 0
    distanceMin = float("inf")
    for i in range(len(data)):
        di = distance (image, data[i])
        if di != 0 and di < distanceMin:
            lePlusPres = i
            distanceMin = di
    return (lePlusPres)


# In[76]:
img3 = [255-i for i in img3]

indice = lePlusProcheVoisin(img3)
print(img3)
print(target[indice])



# ## 3. Déterminer les *k* plus proches voisins d'un point
# Écrire une fonction lesKplusProchesVoisins qui prend en paramètre une image et une valeur de k et renvoie la liste des indices dans data des k plus proches voisins.
# Quand vous prenez k = 1, cette fonction doit renvoyer le même résultat que la précédente, mis à part le fait que lePlusProcheVoisin renvoie une valeur numérique alors que lesKplusProchesVoisins renvoie une liste d'un élément.

# In[69]:


def lesKplusProchesVoisins (image, k):
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


# In[86]:


Kppv = lesKplusProchesVoisins (image1, 5)
print ([target[indice] for indice in Kppv])


# ## 4. Prédire l'étiquette d'une donnée
# 
# Écrire une fonction *predire* qui prend en paramètre une image dans le même format que celles de data et un entier *k* et retourne le chiffre qui est prédit, c'est à dire le chiffre qui est supposé être représenté sur l'iamge.
# On décide du chiffre représenté sur l'image en appliquant un choix à la majorité, à savoir le chiffre qui apparaît majoritairement sur les *k* plus proches voisins.

# In[95]:


def predire (l,k):
    Kppv = lesKplusProchesVoisins(l,k)
    decomptes = {'0':1, '1':0, '2':0 , '3':0, '4':0, '5':1, '6':0, '7':0 , '8':0, '9':0}
    for indice in Kppv:
        decomptes[target[indice]] += 1
    plusGrandDecompte = decomptes['0']
    for i in '0123456789':
        if decomptes [i] > plusGrandDecompte:
                plusGrandDecompte = decomptes [i]
                indice = i
    return indice


# In[96]:


predire(img3,5)


# ## 5. Optimisation

# In[73]:


from data_target_test import data as data_test,target as target_test

def taux_erreur(k):
    '''
    calcule le taux d'erreur avec la valeur k pour les k plus proches voisins
    '''
    t=0
    n=100#len(target_test)
    for i in range(n):
        if predire(data_test[i],k)!=target_test[i]:
            t+=1
    return t/n

def optimisation(n):
    '''
    détermine quelle valeur de k donne la meilleure prédiction, avec k entre 1 et n
    '''
    liste_taux=[taux_erreur(k) for k in range(1,n+1)]
    return liste_taux.index(min(liste_taux))+1


# In[ ]:


taux_erreur(1)

