from random import sample
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, cache=True) # téléchargement de la base complète

N=6000 # nombre total d’éléments pris
n=5000 # nombre dans la base d'apprentissage ; N-n est alors le nombre dans la base de test

l=sample(range(70000),N) # liste d’indices pris au hasard

data=[mnist.data[i].astype(int).tolist() for i in l] # données (images sous forme de listes)
target=[int(mnist.target[i]) for i in l] # valeurs cibles des images

file=open("data_target.py",'w') # base d’apprentissage
file.write("data=")
file.write(str(data[0:n]))
file.write("\ntarget=")
file.write(str(target[0:n]))
file.write("\n")
file.close()

file=open("data_target_test.py",'w') # base de test
file.write("data_test=")
file.write(str(data[n:]))
file.write("\ntarget_test=")
file.write(str(target[n:]))
file.write("\n")
file.close()
