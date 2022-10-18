prenom = "Pierre"
age = 20
isMajeur = True
compte_en_banque = 20135.384
amis = ['Marie', 'Julien','Adrien']
parent = ('Marc','Caroline')
variableWord = 'ami'

if isMajeur == True:
    isMajeur = str('majeur')

else : 
    isMajeur = str('mineur')

if len(amis) > 1 :
    variableWord = 'amis'

print(isinstance(prenom,str))

print(prenom,' agé de ',age,' ans. Déclaré ', isMajeur, ' possède ', compte_en_banque , '$. Ayant', len(amis) , 'amis.')