import sys
choix = 0
liste = []
print("\r\n\r\n")
print("Liste des courses v0.0.1")
print("Menu : ")
print("1. Ajouter un élément à la liste de courses")
print("2. Retirer un élément de la liste de courses")
print("3. Afficher la liste de courses")
print("4. Vider la liste de courses")
print("5. Quitter le programme")
print("6. Afficher le menu")

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
        continue
    elif(choix == "6"):
        print("\r\n\r\n")
        print("Liste des courses v0.0.1")
        print("Menu : ")
        print("1. Ajouter un élément à la liste de courses")
        print("2. Retirer un élément de la liste de courses")
        print("3. Afficher la liste de courses")
        print("4. Vider la liste de courses")
        print("5. Quitter le programme")
        print("h. Afficher le menu")
    else:
        print("\r\n\r\n")
        print('/!\\ Choix non valide \/!\\')
        print("\r\n\r\n")

        print("Liste des courses v0.0.1")
        print("Menu : ")
        print("1. Ajouter un élément à la liste de courses")
        print("2. Retirer un élément de la liste de courses")
        print("3. Afficher la liste de courses")
        print("4. Vider la liste de courses")
        print("5. Quitter le programme")
        print("h. Afficher le menu")

sys.exit()