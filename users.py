from data import *
#1. Filtrer les utilisateurs majeurs (filter).
# def filtrer_majeur(user):
#  utilisateurs_majeurs = list(filter(lambda user : user[3] >= 18, utilisateurs))
#  print(utilisateurs_majeurs)
# # filtrer_majeur(utilisateurs)

# #2. Formater les noms complets en majuscules (map, lambda).
# def noms_complets_majuscule():
#     noms_majuscule = list(map(lambda user : user[1].upper(), utilisateurs))
#     print(noms_majuscule)
# # noms_complets_majuscule()

# # 3. Créer un dictionnaire associant chaque utilisateur à ses livres aimés.
# def utilisateurs_livres():
#     user_likes = {}
#     for user in utilisateurs:
#         user_id = user[0]
#         user_name = f"{user[1]} {user[2]} "
#         liked_books = list(map(lambda like: like[1], filter(lambda like: like[0] == user_id, aime_livres)))
#         # user_likes = f"{user_name} a aime : {liked_books}"
#         user_likes[user_name] = liked_books
#     print(user_likes)
# utilisateurs_livres()

# #● Générer un résumé par utilisateur : "ALICE DUPONT (25 ans) aime : '1984', 'Le Petit Prince'"
# def resume_par_utilisateur ():
#     List = []
#     for user in utilisateurs:
#         user_id = user[0]
#         user_name = f"{user[1]} {user[2]} "
#         user_age = user[3]
#         liked_books = list(map(lambda like: like[1], filter(lambda like: like[0] == user_id, aime_livres)))
#         if liked_books:
#           resume = f"{user_name}({user_age}) aime : {liked_books}"
#         else:
#           resume = f"{user_name}({user_age}) n'aime pas aucun livres."
#         List.append(resume)
#     print(List)
# resume_par_utilisateur()


    # for user in utilisateurs:
    #     user_id = user[0]
    #     user_name = f"{user[1].upper()} {user[2].upper()} ({user[3]} ans)"
    #     liked_books = list(map(lambda like: like[1], filter(lambda like: like[0] == user_id, aime_livres)))
    #     livres_aimes = ', '.join(f"'{book}'" for book in liked_books)
    #     print(f"{user_name} aime : {livres_aimes}")

#Construire un dictionnaire :{ "1984": 2, "Le Petit Prince": 1, "Harry Potter": 1 }
# def livres_populaires():
#     livres_count = {}
#     for livre in aime_livres:
#         titre = livre[1]
#         count = sum(1 for like in aime_livres if like[1] == titre)
#         livres_count[titre] = count
#     print(livres_count)
# livres_populaires()
List = []
for tupe in aime_livres:
    titre = tupe[1]
    count = 0   # ✅ reset once per title
    for like in aime_livres:
        if like[1] == titre:
            count += 1
    var = f"{titre} : {count}"
    List.append(var)

print(List)



