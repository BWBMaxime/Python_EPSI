#print('Hello World')

#Premier commentaire

x = 5 #Déclaration de variable (pas forcément de type déclarer) automatiquement "int"
#print(x)

"""
Comentaires
MultiLigne
:p
"""

#Casting
str = str(5)
int = int(10)
float = float(15)

#print(str,int,float)

#Ressortir le type de la variable (principalement pour test)
#print(type(str))

#multiple assignation
fruit,legume = "pomme","tomate"
#print(fruit,legume)

#collection liste. J'affecte a,b,c au index du tableau

fruits = ['pomme', 'poire','melon']
a,b,c = fruits

#print(a)
#print(b)
#print(c)

#Variable globale

globale = "I m Global"

def firstFunction():
     global globale
     globale = "I m New Gloable"

#appel de fonction qui retourne la variable Local
firstFunction()
#Retourn la variable en global
#print(globale)

"""
str = chaine de caractère
numeric = int,float,complexe
sequence = list,tuple,range
mapping type = dict
set Types = set frozenSet
bool
binary = bytes memoryview
None type

tuple = ("fruits","legumes")

range = range(6) 

dictLa majusculee reste
x={"nom":"Artz", "Age":40}

set = {"fruits","legume"}

pour le float on peut faire x= 37e4 
"""

import random #import de module
#print(random.randrange(1,10))

#Tkinter = Interface graphique en python (lourd et pas terrible mais alternative = PyWT5 / PySide2)

from math import factorial

#print(factorial(5))

#boucle for

for x in 'Maxime':
    print(x)

# Décla de class
# class maClass():
#     def __len__(self):
#         return 0

# monObjet = maClass()
# print(bool(monObjet))
# choisisTonMot = input('Choisis ton salut : ')
# txt = '{} tout le monde.'
# print(txt.format(choisisTonMot))


# list = ['Pierre', 'Julien', 'Anne', 'Marie', 'Lucien']
# list.sort()
# print(list)
