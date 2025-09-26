from data import *
#Qstion 1
utilisateurs_majeurs = list(filter(lambda user : user[3] >= 18, utilisateurs))
print(utilisateurs_majeurs)
#Qstion 2
noms_majuscule = list(map(lambda user : user[1].upper(), utilisateurs))
print(noms_majuscule)
#Qstion 3

