file = input("Entrer le chemin vers le fichier : ")

try:
    f = open(file, encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print("Le fichier indique est introuvable")
except UnicodeDecodeError:
    print("Le format du fichier n'est pas supporte")
else:
    f.close()