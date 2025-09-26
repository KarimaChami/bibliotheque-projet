from data import *

livres_trier = sorted(livres, key=lambda x: x["année"])
print(livres_trier)

print(f"le livre le plus ancien est : {livres_trier[0]["titre"]} et le livre le plus resent est : {livres_trier[2]["titre"]} ")

