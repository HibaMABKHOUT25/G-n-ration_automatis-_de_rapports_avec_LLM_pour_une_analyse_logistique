# Génération automatisée de rapports avec _LLM_ pour une analyse logistique
Dans le cadre d’un projet d’optimisation de la logistique last-mile, les prévisions de demande (déjà générées) et les itinéraires optimisés (via un algorithme ACO – Ant Colony Optimization) ont été exploités pour analyser la répartition des livraisons et l’efficacité de la flotte dans la zone urbaine étendue de Casablanca.
Objectifs :

Identifier les clients les plus demandeurs et les jours de forte activité
Analyser l’utilisation de la flotte (taux de remplissage, distances, émissions)
Détecter les véhicules sous-utilisés
Automatiser la génération d’un rapport professionnel à partir des données et d’un LLM local

Stack technique :

Langage : Python
Bibliothèques : Pandas, Requests
Prévision : (données déjà prédites)
Optimisation : Algorithme ACO (résultats déjà calculés)
IA Générative : Ollama API (Mistral)
Formats : Excel (entrée), TXT (rapport final)

Réalisations :

Lecture et traitement de données Excel
Extraction de KPIs logistiques : top 5 clients, top 3 jours de forte demande, distances moyennes, émissions moyennes
Détection automatique des véhicules sous-utilisés (< 20 % de charge)

Création d’un prompt structuré guidant le LLM pour produire un rapport clair et professionnel

Génération et sauvegarde automatique du rapport
