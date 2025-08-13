import pandas as pd
import requests

# Lire les fichiers Excel
df_forecast = pd.read_excel(r"C:\Users\ASUS\Desktop\Documentation PFE\Reporting\demandes clients merg 80 reporting.xlsx")
df_aco = pd.read_excel(r"C:\Users\ASUS\Desktop\Documentation PFE\Reporting\Resultats ACO 80 clients.xlsx")

# Correction : Convertir la colonne en numérique
df_aco["Charge utilisée (%)"] = pd.to_numeric(df_aco["Charge utilisée (%)"], errors='coerce')

# Clients les plus demandés
moyennes_clients = df_forecast.iloc[:, 1:].mean().sort_values(ascending=False).head(5)
clients_plus_demandes = "\n".join([f"{k} : {round(v, 2)}" for k, v in moyennes_clients.items()])

# Jours de forte demande
df_forecast["total"] = df_forecast.iloc[:, 1:].sum(axis=1)
top_jours = df_forecast.sort_values("total", ascending=False).head(3)
pics = "\n".join([f"{d['date'].strftime('%Y-%m-%d')} : {round(d['total'], 2)}" for _, d in top_jours.iterrows()])

# Moyennes ACO
moy_dist = round(df_aco["Distance (km)"].mean(), 2)
moy_emis = round(df_aco["Émissions (g)"].mean(), 2)

# Véhicules sous-utilisés (< 20 %)
sous_utilisation = df_aco[df_aco["Charge utilisée (%)"] < 20]
if sous_utilisation.empty:
    vehicules_sous_utilises = "Aucun véhicule sous-utilisé détecté."
else:
    vehicules_sous_utilises = sous_utilisation.to_string(index=False)

# Prompt LLM enrichi avec précisions
prompt = f"""
Voici une analyse logistique basée sur des prévisions de livraison et des résultats d’optimisation (ACO) pour 80 clients dans la zone urbaine étendue de Casablanca.

 Clients les plus demandés :
{clients_plus_demandes}

 Jours de demande exceptionnelle :
{pics}

 Optimisation ACO :
- Moyenne des distances : {moy_dist} km
- Moyenne des émissions de CO2 : {moy_emis} g
- Véhicules sous-utilisés (<20 %) :
{vehicules_sous_utilises}

 Contexte :
- Les données de demande sont **déjà des prévisions produites par le modèle Prophet**.
- Les itinéraires ont été **déjà optimisés par un algorithme de colonies de fourmis (ACO)**.
- Casablanca est une métropole étendue, ce qui explique des distances importantes sans inefficacité.

 Ne pas proposer de :
- Réoptimiser les trajets (déjà fait par ACO)
- Ajouter des prévisions de demande (déjà fait par Prophet)

 Se concentrer sur :
- L’interprétation des résultats
- Le dimensionnement de la flotte
- L’impact environnemental
- Des recommandations **réalistes et complémentaires**

Merci de rédiger un rapport professionnel (2 à 3 paragraphes) :
- Analyse la répartition de la demande (basée sur les prévisions)
- Commente l’utilisation de la flotte (remplissage, distances, émissions)
- Ne critique pas les distances ou les émissions si elles sont cohérentes avec le contexte
- Propose 2 recommandations concrètes et utiles
- Adopte un ton adapté à un rapport de stage
"""

# Envoi de la requête à Ollama local (Mistral)
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
)

# Résultat
texte = response.json()["response"]

# Enregistrer dans un fichier texte
with open("rapport_llm3_genere.txt", "w", encoding="utf-8") as f:
    f.write(texte)

# Affichage console
print("\n Rapport généré automatiquement :\n")
print(texte)
print("\n Rapport sauvegardé dans : rapport_llm3_genere.txt")
