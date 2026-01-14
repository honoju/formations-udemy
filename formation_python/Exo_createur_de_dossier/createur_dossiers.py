from pathlib import Path

chemin = Path.cwd()
    
d = {"Films": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
        "Employes": ["Paul",
                    "Pierre",
                    "Marie"],
        "Exercices": ["les_variables",
                    "les_fichiers",
                    "les_boucles"]}

for key in d:
    dossier_parent = chemin / key
    dossier_parent.mkdir(parents=True, exist_ok=True)
    for item in d[key]:
        dossier_enfant = dossier_parent / item
        dossier_enfant.mkdir(parents=True, exist_ok=True)