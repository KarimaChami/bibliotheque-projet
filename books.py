from data import *

livres_trier = sorted(livres, key=lambda x: x["année"])
print(livres_trier)


print(f"le livre le plus ancien est : {livres_trier[0]["titre"]} et le livre le plus resent est : {livres_trier[2]["titre"]} ")

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
print(Count_List)

 
# while True:
#     numero_page = int(input("Enter le numero de la page : "))
#     page1 = utilisateurs[0:2]
#     page2 = utilisateurs[2:]

#     if numero_page == 1:
#         print(page1)
#     elif numero_page == 2:
#         print(page2)
#     else:
#         print("page not found")
#         break



taille_page = 2

while True:
    page = int(input("Etrer le numero de la page : "))
    debut = (page - 1) * taille_page
    fin = debut + taille_page
    if page == 1 or page == 2:     
        print(utilisateurs[debut:fin])
    else:
        print("page not found!")
        break







   