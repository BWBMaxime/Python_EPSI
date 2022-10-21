# # --------------------------------------------------------------------------------
# list1 = ['Marie', 'Julien','Adrien']
# list1.remove(list1[1])
# print(list1)
# # --------------------------------------------------------------------------------
# for x in 'Maxime':
#     print(x)
# # --------------------------------------------------------------------------------
# a = "Bonjour"
# print(a.replace("Bonjour", "Bonsoir"))
# # --------------------------------------------------------------------------------
# def sortByAlphabeticalOrder(prenoms):
#   textArray = prenoms.split(", ")
#   return ", ".join(sorted(textArray))

# print(sortByAlphabeticalOrder("Pierre, Julien, Anne, Marie, Lulien"))
# # --------------------------------------------------------------------------------
# from math import pi

# rayon = int(10)

# volume = (4.0 * pi / 3.0) * (rayon ** 3)

# print(volume)
# # --------------------------------------------------------------------------------
# numberChoice = int(input("Choisis un nombre :"))
# lst = []
# def createList(n):
   
#     if numberChoice > 15 :
#         print('Nombre trop grand')
#     else :
#         for i in range(5,n+1):
#           lst.append(i)
#           return(lst)

# print(createList(numberChoice)) 
# # --------------------------------------------------------------------------------
# def maFonct(n) :
#   return abs(n-50)

# number = [100, 52, 88,27,50,788]
# number.sort(key = maFonct)
# print(number)
# # --------------------------------------------------------------------------------
# maliste = ["banane","fraise","mangue"]
# maliste.sort(reverse = True)
# print(maliste)
# # --------------------------------------------------------------------------------
#tuple
# montuple = ("pomme","fraise","citron")
# print(montuple)

# --------------------------------------------------------------------------------
# for x in liste2:
#     liste1.append(x)
# print(liste1)

# --------------------------------------------------------------------------------
#liste1.extend(liste1)

# clear() va vider la liste
# liste1.clear()
# print(liste1)

# --------------------------------------------------------------------------------
# les TUPLES
# montuple = ('pomme','babane','kiwi')
# print(len(montuple))
# print(type(montuple))

# --------------------------------------------------------------------------------
# creer un tuple avec un objet
# montuple = ('poire',)
# print(type(montuple))
# on peut mélanger les types et avoir des tuples constituer de boolean,chaine,entier, etc
# le tuple est une classe comme les autres types en python
# faire appel au constructeur du tuple

# --------------------------------------------------------------------------------
# montuple= tuple(("pomme","poire","kiwi"))
# print(montuple)
# print(montuple[1])


# montuple = ('poire','banane','pomme','kiwi','citron')
# # print(montuple[2:5])
# # if 'citron' in montuple:
# #     print('oui il y a du citron')
# a=list(montuple)
# a[1] = 'fraise'
# montuple = tuple(a)
# print(montuple)
# a =("fraisexmamkf",)

# montuple += a
# print(montuple)
# # --------------------------------------------------------------------------------
# for x in range(len(montuple)):
#   print(x)
# i = 0
# while i < len(montuple):
#   i = i + 1
#   print(i)

# Exercice : construit un code qui affiche un liste des nombres pairs de 1 a 100
# liste_nombre_pairs = range(2, 101, 2)
# resultat = list(liste_nombre_pairs)
# print(resultat)
# # Exercice : Affiche 6 lancé aléatoire d un dés
import random

# lancers = []
# for _ in range(6):
#     nombre = random.choice(range(1, 7))
#     lancers.append(nombre)
# print(lancers)

# Exercice : générer un nombre de lancé de dès choisis par l'utilisateur et afficher la moyenne en flottant de l'enssemble des lancé
# lancers = []
# numberChoice = int(input("Choisis un nombre de lancé : "))
# for x in range(numberChoice):
#     nombre = random.choice(range(1, 7))
#     lancers.append(nombre)
#     moyenneInFloat = sum(lancers) / len(lancers)
# print(moyenneInFloat)

lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"

def compter(lettre_a_chercher,phrase):
    compteur = 0
    for L in phrase.lower() :
        if L == lettre_a_chercher :
            compteur = compteur + 1
    return compteur

print(compter(lettre_a_chercher,phrase))

import mesTest 

mesTest.isMyFriend()
