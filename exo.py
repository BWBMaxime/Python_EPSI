prenom = str("Pierre")
age = int(20)
isMajeur = bool(False)
compte_en_banque = float(20135.384)
amis = ['Marie', 'Julien','Adrien']
parents = ["Marc","Caroline"]
mere = parents[1]
pere = parents[0]
variableWord = str('ami.')
nbAmis= int(len(amis))

presentation = str('{} agé de {} ans. Déclaré {} possède {} $. Ayant {} {} Et comme père {} et mère {}.')

if isMajeur == True:
    isMajeur = str('majeur')

else : 
    isMajeur = str('mineur')

if nbAmis > 1 :
    variableWord = str('amis.')

# print(isinstance(prenom,str))

#print(prenom,' agé de ',age,' ans. Déclaré ', isMajeur, ' possède ', compte_en_banque , '$. Ayant', nbAmis , variableWord)
print(presentation.format(prenom,age,isMajeur,compte_en_banque,nbAmis,variableWord,pere,mere))
# yourName = input('Enter your name !')

# print('Ton nom est', yourName,'.')


