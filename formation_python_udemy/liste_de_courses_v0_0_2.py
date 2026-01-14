import sys
import json
from pathlib import Path

JSON_FILE = "liste_de_courses.json"

p = Path(JSON_FILE)
choix = 0
liste = []
MENU='''
\r\n
Liste des courses v0.0.1"
Menu :
1. Ajouter un élément à la liste de courses
2. Retirer un élément de la liste de courses
3. Afficher la liste de courses
4. Vider la liste de courses
5. Quitter le programme
6. Afficher le menu
\r\n
'''

if (not p.exists()) or (p.stat().st_size == 0):
    p.touch()
    with p.open("w", encoding="utf-8") as f:
        json.dump(liste, f, indent=4)

with p.open("r", encoding="utf-8") as f:
    liste = json.load(f)

print(MENU)

while choix != "5":
    print("\r\n\r\n")

    choix = input("Quel est votre choix : ")

    if (choix == "1" ):
        entree = input("Que voulez-vous ajouter à la liste : ")
        liste.append(entree)
    elif (choix == "2" ):
        entree = input("Quel élément voulez-vous retirer : ")
        if entree in liste:
            liste.remove(entree)
            print("\r\n\r\nVotre liste de courses")
            print("======================")
            for i,element in enumerate(liste):
                print(f"{i+1} . {element}")
        else:
            print(f"\r\n\r\n{entree} n'est pas dans la liste")
    elif (choix == "3" ):
        if(len(liste) == 0):
            print("\r\n\r\nVotre liste est vide pour le moment")
        else:
            print("\r\n\r\nVotre liste de courses")
            print("======================")
            for i,element in enumerate(liste):
                print(f"{i+1} . {element}")
    elif(choix == "4"):
        liste.clear()
    elif(choix == "5"):
        with p.open("w", encoding="utf-8") as f:
            json.dump(liste, f, indent=4)
        continue
    elif(choix == "6"):
        print(MENU)
    else:
        print("\r\n\r\n")
        print('/!\\ Choix non valide \/!\\')

        print(MENU)

sys.exit()