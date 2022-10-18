# Déclarations Variables
# prenom = str("Pierre")
# age = int(10)
# isMajeur = bool(False)
# compte_en_banque = float(20135.384)
# amis = ['Marie', 'Julien','Adrien']
# parents = ["Marc","Caroline"]
# mere = parents[1]
# pere = parents[0]
# variableWord = str('ami.')
# nbAmis= int(len(amis))

# presentation = str('Salut, moi c est {} agé de {} ans. Ayant {} {} Mes parents sont {} et {}. Veux tu être mon ami ?')
# thanks = str('Merci pour tes infos, je note : Monsieur {}, agé de {} ans et résidant au {}. Merci pour tes {} $ pris sur ton compte ;) .')
# noThanks = str('Monsieur {}, agé de {} ans et résidant au {}. Les moins de 10 ca dégage. Toi = {} = - de 10.')

# def isPresentation() :
#     if nbAmis > 1 :
#         variableWord = str('amis.')

#     print(presentation.format(prenom,age,compte_en_banque,nbAmis,variableWord,pere,mere))
#     global isFriend
#     isFriend = input("( y/n )")

# def isMyFriend():
#     if isFriend == 'y' :
#         yourName, yourAge, yourAdress, yourSolde = input('Entre ton nom :'), input('Entre ton age : '), input('Entre ton adresse : '), input('Entre ton solde de compte : ')
#         if age < 18:
#             isMajeur = False
#         else :
#             isMajeur = True
#         if isMajeur == True:
#             isMajeur = str('majeur')

#         else : 
#             isMajeur = str('mineur')

      
#         # print(isinstance(prenom,str))
#         #print(prenom,' agé de ',age,' ans. Déclaré ', isMajeur, ' possède ', compte_en_banque , '$. Ayant', nbAmis , variableWord)
#         if int(yourSolde) < 10000:
#             print(noThanks.format(yourName,yourAge,yourAdress,yourSolde))
#         else : 
#             print(thanks.format(yourName,yourAge,yourAdress,yourSolde))
#     else : 
#         print('Bravo Inconnu, tu ne t es pas fais piègé et je n ai donc pas enregistrer tes données personnel')

# isPresentation()
# isMyFriend()

# list1 = ['Marie', 'Julien','Adrien']
# list1.remove(list1[1])
# print(list1)
