# --------------------------------------------------------------------------------
list1 = ['Marie', 'Julien','Adrien']
list1.remove(list1[1])
print(list1)
# --------------------------------------------------------------------------------
for x in 'Maxime':
    print(x)
# --------------------------------------------------------------------------------
a = "Bonjour"
print(a.replace("Bonjour", "Bonsoir"))
# --------------------------------------------------------------------------------
def sortByAlphabeticalOrder(prenoms):
  textArray = prenoms.split(", ")
  return ", ".join(sorted(textArray))

print(sortByAlphabeticalOrder("Pierre, Julien, Anne, Marie, Lulien"))
# --------------------------------------------------------------------------------
from math import pi

rayon = int(10)

volume = (4.0 * pi / 3.0) * (rayon ** 3)

print(volume)
# --------------------------------------------------------------------------------
numberChoice = int(input("Choisis un nombre :"))
lst = []
def createList(n):
   
    if numberChoice > 15 :
        print('Nombre trop grand')
    else :
        for i in range(5,n+1):
          lst.append(i)
          return(lst)

print(createList(numberChoice)) 
# --------------------------------------------------------------------------------
def maFonct(n) :
  return abs(n-50)

number = [100, 52, 88,27,50,788]
number.sort(key = maFonct)
print(number)
# --------------------------------------------------------------------------------