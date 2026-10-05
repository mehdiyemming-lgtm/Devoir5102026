from pathlib import Path

FICHIER = "journal.txt"

# 1. Vérifier si le fichier existe déjà
if not Path(FICHIER).exists():

    # 2. Demander trois titres avec une boucle for et range(3)
    titres = []
    for i in range(3):
        titre = input(f"Titre {i + 1} : ")
        titres.append(titre)

    # 3. Écrire chaque titre dans le fichier, en mode w
    with open(FICHIER, "w", encoding="utf-8") as fichier:
        for titre in titres:
            fichier.write(titre + "\n")

    print(f"\n{FICHIER} créé avec 3 titres.")

else:
    print(f"{FICHIER} existe déjà.")
    T= input ("Entrez un titre")
    with open(FICHIER, "a", encoding="utf-8") as fichier:
        fichier.write(T + "\n")


# Rappel des modes d'ouverture de fichier :
# "w" (write)  -> crée le fichier s'il n'existe pas, ou écrase tout son contenu s'il existe déjà
# "a" (append) -> ajoute du texte à la fin du fichier sans effacer ce qui existe déjà
# "r" (read)   -> ouvre le fichier en le lisant, mais ne permet pas d'écrire dedans

print("\n--- Contenu du journal ---")
with open(FICHIER, "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne, end="")