import csv

def exporter_csv(taches, chemin):
    with open(chemin, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=["titre", "faite"])
        writer.writeheader()

        for tache in taches:
            writer.writerow(tache)