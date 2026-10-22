# Objectif : webscrapper la map du 17 octobre
# task 1 : catégories d'évènements (rond points, manifs, sit-ins)
# task 2 : informations s/ actions (nb de participants p ex)

# Débuts 
from bs4 import BeautifulSoup
import requests

# 1. URL de la page cible
url = "https://www.17octobregiletjaune.net/carte/17-octobre/"

# 2. Ajouter des en-têtes (Headers) pour simuler un vrai navigateur 
# (évite parfois d'être bloqué par une protection anti-bot basique)
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

try:
  # Envoyer la requête HTTP GET
  response = requests.get(url, headers=headers)
  response.raise_for_status()  # Vérifie si la requête a réussi (code 200)

  # Analyser le contenu HTML avec BeautifulSoup
  soup = BeautifulSoup(response.text, "html.parser")

  # Exemple A : Récupérer le titre de la page
  titre = soup.find("title")
  if titre:
    print(f"Titre de la page : {titre.text.strip()}")

  # Exemple B : Rechercher un texte spécifique (ex: les mobilisations recensées)
  # Utilisez l'inspecteur de votre navigateur pour trouver la balise et la classe exacte (ex: div, span, p)
  # Ici, on cherche par exemple tous les paragraphes ou blocs de texte contenant des chiffres
  print("\n--- Analyse du texte brut récupéré ---")
  texte_global = soup.get_text()

  # Pour afficher un extrait ou chercher un mot-clé particulier :
  if "mobilisations recensées" in texte_global:
    print("Le texte 'mobilisations recensées' a bien été trouvé dans le HTML statique.")

  # Exemple C : Extraire tous les liens (balises <a>) de la page
  print("\n--- Liste de quelques liens trouvés ---")
  for link in soup.find_all("api") or soup.find_all("a", href=True):
    # Vous pouvez filtrer les liens ici
    pass

except requests.exceptions.RequestException as e:
  print(f"Erreur lors de la requête HTTP : {e}")

  # Rechercher toutes les balises <script> pour voir si les données y sont stockées
scripts = soup.find_all("script")
print(f"Nombre de balises script trouvées : {len(scripts)}")

for i, script in enumerate(scripts):
  if script.string and ("mobilisation" in script.string or "lat" in script.string):
    print(
        f"La balise script n°{i} contient potentiellement des données de"
        " géolocalisation ou de mobilisations !"
    )
    # Vous pouvez afficher un extrait pour voir à quoi ça ressemble :
    # print(script.string[:500])