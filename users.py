from data import *

utilisateurs_majeurs = list(filter(lambda user : user[3] >= 18, utilisateurs))
print(utilisateurs_majeurs)