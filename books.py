from data import *

livres_trier = sorted(livres, key=lambda x: x["année"])


print(f"le livre le plus ancien est : {livres_trier[0]["titre"]} et le livre le plus resent est : {livres_trier[2]["titre"]} ")

# dictionnaire = dict(aime_livres)
# print(dictionnaire)
List = []
for tup in aime_livres:
    List.append(tup[1])

Count_List = []  
itereted_items = []
for L in List:   
    a = List.count(L)
    if L not in itereted_items:
        Count_List.append(a)
    itereted_items.append(L)




    """ titre_livre = tup[1]
    print(titre)
    user_id = 0
    if titre_livre == titre_livre:
      user_id += 1
      txt = f"{titre_livre }:{user_id}"
    List.append(txt) """