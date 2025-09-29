utilisateurs = [
(1, "Alice", "Dupont", 25),
(2, "Bob", "Martin", 17),
(3, "Clara", "Durand", 32),
(4, "David", "Petit", 20)
]
livres = [
{"titre": "1984", "auteur": "George Orwell", "année": 1949},
{"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "année": 1943},
{"titre": "Harry Potter", "auteur": "J.K. Rowling", "année":1997}
]
aime_livres = [
(1, "1984"),
(1, "Le Petit Prince"),
(3, "Harry Potter"),
(4, "1984")
]

list_tup = []
for tup in aime_livres:
    print(tup[1])
    list_tup.append(tup[1])
print(list_tup)
for livre in list_tup:
    repitition = list_tup.count(livre)
    print(repitition)