import csv
import json

nom_json = 'lieux.json'
nom_csv = 'lieux.csv'

print(f"1. Tentative de lecture du fichier : {nom_json}")

try:
  with open(nom_json, 'r', encoding='utf-8') as f:
    data = json.load(f)
except Exception as e:
  print(f"Erreur : Impossible de lire le fichier JSON. ({e})")
  exit()

lignes_a_ecrire = []

if isinstance(data, list):
  print("-> Format détecté : Liste de lieux standard.")
  lignes_a_ecrire = data
elif isinstance(data, dict):
  print("-> Format détecté : Dictionnaire de lieux par ID.")
  for cle_id, info_lieu in data.items():
    if isinstance(info_lieu, dict):
      if 'id' not in info_lieu:
        info_lieu['id'] = cle_id
      lignes_a_ecrire.append(info_lieu)

if not lignes_a_ecrire:
  print(
      "Le fichier a bien été ouvert, mais aucune donnée exploitable n'a"
      " été trouvée."
  )
else:
  # CORRECTION : On collecte TOUTES les clés uniques de TOUS les objets du JSON
  toutes_les_cles = set()
  for ligne in lignes_a_ecrire:
    if isinstance(ligne, dict):
      toutes_les_cles.update(ligne.keys())

  enquetes_headers = list(toutes_les_cles)

  # Écriture du fichier CSV
  with open(nom_csv, 'w', newline='', encoding='utf-8-sig') as f_csv:
    writer = csv.DictWriter(
        f_csv, fieldnames=enquetes_headers, extrasaction='ignore'
    )
    writer.writeheader()
    writer.writerows(lignes_a_ecrire)

  print(
      f"fichier CSV des lieux a été généré ici : '{nom_csv}'"
      f" avec {len(lignes_a_ecrire)} lignes."
  )
