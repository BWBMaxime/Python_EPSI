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


montuple = ('poire','banane','pomme','kiwi','citron')
# print(montuple[2:5])
# if 'citron' in montuple:
#     print('oui il y a du citron')
a=list(montuple)
a[1] = 'fraise'
montuple = tuple(a)
print(montuple)
a =("fraisexmamkf",)

montuple += a
print(montuple)
# --------------------------------------------------------------------------------
for x in range(len(montuple)):
  print(x)
i = 0
while i < len(montuple):
  i = i + 1
  print(i)