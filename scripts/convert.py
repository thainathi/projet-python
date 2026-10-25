import csv
import json 
import os

# Détecte automatiquement le dossier où se trouve ce script Python
dossier_script = os.path.dirname(os.path.abspath(__file__))
fichier_json = os.path.join(dossier_script, "donnees.json")
fichier_csv = os.path.join(dossier_script, "donnees.csv")

fichier_json = 'actions.json'
fichier_csv = 'actions.csv'

print ("Lecture du fichier JSON...")
with open(fichier_json, 'r', encoding='utf-8') as f: 
    data = json-load(f)

