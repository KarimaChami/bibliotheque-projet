from data import *
#1. Filtrer les utilisateurs majeurs (filter).
def filtrer_majeur(user):
 utilisateurs_majeurs = list(filter(lambda user : user[3] >= 18, utilisateurs))
 print(utilisateurs_majeurs)
# filtrer_majeur(utilisateurs)

#2. Formater les noms complets en majuscules (map, lambda).
def noms_complets_majuscule():
    noms_majuscule = list(map(lambda user : user[1].upper(), utilisateurs))
    print(noms_majuscule)
# noms_complets_majuscule()

# 3. Créer un dictionnaire associant chaque utilisateur à ses livres aimés.
def utilisateurs_livres():
    user_likes = {}
    for user in utilisateurs:
        user_id = user[0]
        user_name = f"{user[1]} {user[2]}"
        liked_books = list(map(lambda like: like[1], filter(lambda like: like[0] == user_id, aime_livres)))
        user_likes[user_name] = liked_books
    print(user_likes)
utilisateurs_livres()
# 1. Trier les livres par année de publication (sort)
def trier_livres():
    livres_tries = sorted(livres, key=lambda livre: livre["année"])
    print(livres_tries)

trier_livres()