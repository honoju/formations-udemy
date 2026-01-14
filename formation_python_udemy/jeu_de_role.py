import random

vie_heros = 50
vie_ennemi = 50
potions_heros = 3
mystere = random.randint(0,100)

print("Bienvenu dans le jeu de role.")

while((vie_heros > 0) and (vie_ennemi > 0)):
    strat = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? :")
    while((strat.isdigit() == False) or (int(strat) not in [1,2])):
        strat = input("Entrez un choix valide(1 ou 2) : ")
    
    if(int(strat) == 1):
        vie_ennemi -= random.randint(5,10)
        vie_heros -= random.randint(5,15)
        if((vie_heros > 0) and (vie_ennemi > 0)):
            print(f"Apres attaques mutuelles ⚔️, il vous reste {vie_heros} ❤️")
            print(f"Apres attaques mutuelles ⚔️, il reste {vie_ennemi} ❤️ a votre adversaire")
    elif(int(strat) == 2):
        if(potions_heros == 0):
            print("Vous n'avez plus de potions ...")
        else:
            potions_heros -= 1
            regain = random.randint(15, 49)
            print(f"La potion vous donne {regain} ❤️ supplementaires")
            vie_heros = min(50, regain + vie_heros)
            print(f"Vous avez maintenant {vie_heros} ❤️")
            vie_heros -= random.randint(5,15)
            vie_heros -= random.randint(5,15)
            print(f"L'adversaire vous a attaqué 2 fois ⚔️⚔️. Il vous reste {vie_heros} vies")
            print(f"Il reste {vie_ennemi} ❤️ a votre adversaire")
    
    print("------------------------------------------------------------------")

if(vie_ennemi <= 0):
    print("Vous avez gagne")
else:
    print("Vous avez perdu")