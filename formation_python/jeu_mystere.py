import random

nb_essais = 5
resultat = False
mystere = random.randint(0,100)

print("Bienvenu dans le jeu du nombre mystere. Devinez le nombre compris entre 0 et 100")

while((nb_essais > 0) and (resultat == False)):
    print(f"Il vous reste {nb_essais} essai(s)")
    prop = input("Faites votre proposition :")
    while((prop.isdigit() == False) or (int(prop) > 100)):
        prop = input("Entrez une valeur valide(un nombre compris entre 0 et 100) : ")
    
    if(int(prop) < mystere):
        print(f"Le nombre mystere est superieur a {prop}")
        nb_essais -= 1
    elif(int(prop) > mystere):
        print(f"Le nombre mystere est inferieur a {prop}")
        nb_essais -= 1
    elif(int(prop) == mystere):
        print(f"Bravo, vous avez trouve le nombre mystere en {5-(nb_essais-1)} coup(s)")
        resultat = True
        
if(nb_essais == 0) and (resultat == False):
    print(f"Vous n'avez pas reussi a trouver le nombre mystere {mystere}")