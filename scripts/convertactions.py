import csv
import json

# Nom de votre fichier JSON d'entrée (modifiez si besoin)
nom_json = 'actions.json'
nom_csv = 'actions.csv'

print(f"1. Tentative de lecture du fichier : {nom_json}")

try:
  with open(nom_json, 'r', encoding='utf-8') as f:
    data = json.load(f)
except Exception as e:
  print(f"Erreur : Impossible de lire le fichier JSON. ({e})")
  exit()

lignes_a_ecrire = []

# Cas 1 : Le JSON est une liste directe d'objets (ex: [ {"id": 1, "titre": "..."}, ... ])
if isinstance(data, list):
  print("-> Format détecté : Liste d'objets standard.")
  lignes_a_ecrire = data

# Cas 2 : Le JSON est un dictionnaire avec des clés (ex: { "id_1": [ [titre, temps, date, montant], ... ] })
elif isinstance(data, dict):
  print('-> Format détecté : Dictionnaire par ID (structure complexe).')
  for id_lieu, actions in data.items():
    if isinstance(actions, list):
      for action in actions:
        # Si chaque action est elle-même une liste [title, time, date, amount]
        if isinstance(action, list):
          lignes_a_ecrire.append({
              'id': id_lieu,
              'title': action[0] if len(action) > 0 else '',
              'time': action[1] if len(action) > 1 else '',
              'date': action[2] if len(action) > 2 else '',
              'amount': action[3] if len(action) > 3 else '',
          })
        # Si chaque action est déjà un dictionnaire
        elif isinstance(action, dict):
          action['id'] = id_lieu
          lignes_a_ecrire.append(action)

# Vérification finale avant l'écriture
if not lignes_a_ecrire:
  print(
      "Le fichier a bien été ouvert, mais aucune donnée exploitable n'a"
      " été trouvée."
  )
else:
  # Récupération automatique des colonnes (en-têtes)
  enquetes_headers = lignes_a_ecrire[0].keys()

  # Écriture du fichier CSV (encodage utf-8-sig parfait pour Excel)
  with open(nom_csv, 'w', newline='', encoding='utf-8-sig') as f_csv:
    writer = csv.DictWriter(f_csv, fieldnames=enquetes_headers)
    writer.writeheader()
    writer.writerows(lignes_a_ecrire)

  print(
      f"fichier CSV a été généré ici : '{nom_csv}' avec"
      f" {len(lignes_a_ecrire)} lignes."
  )