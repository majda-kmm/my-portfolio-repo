import pandas as pd
from sqlalchemy import create_engine
#1. charger et nettoyer consumer_data (on ignore la première ligne vide ou inutile)
consumer_data = pd.read_csv("consumer_data.csv", skiprows=1)

# on va renommer manuellement les colonnes pour qu'elles soient explicites et cohérentes avec les données
consumer_data.columns = ["Country", "Make", "Model", "Year", "Review Score", "Sales Volume"]

# on nettoie les champs texte en les mettant en minuscules et en supprimant les espaces superflus
consumer_data["Make"] = consumer_data["Make"].str.strip().str.lower()

# on renomme 'Year' en 'Review Year' pour clarifier qu'il s'agit de l'année d'évaluation (pour ne pas avoir d'ambiguité quand on fera le join)
consumer_data = consumer_data.rename(columns={"Year": "Review Year"})

# 2. charger et nettoyer car_data 
car_data = pd.read_csv("car_data.csv")

# on renomme les colonnes pour standardiser les noms et rendre facile la jointure
car_data.rename(columns={
    "('Make', 0)": 'Make',
    "('Model', 0)": 'Car Model',
    "('Production Year', 0)": 'Production Year',
    "('Price', 0)": 'Price',
    "('Engine Type', 0)": 'Engine Type'
}, inplace=True)

# nettoyage des valeurs texte
car_data["Make"] = car_data["Make"].str.strip().str.lower()
car_data["Car Model"] = car_data["Car Model"].str.strip().str.lower()

#  3. jointure sur la colonne 'Make' uniquement 
# ici on ne peut pas utiliser le modèle pour la jointure car il est peu fiable côté consumer_data
# on suppose que les scores de review concernent tous les modèles disponibles à ce moment-là pour une marque
merged = pd.merge(consumer_data, car_data, on="Make", how="inner")

# on garde uniquement les lignes où l'année de production est antérieure ou égale à l'année de la review
# cela garantit que le modèle était effectivement disponible à ce moment-là
filtered = merged[merged["Production Year"] <= merged["Review Year"]]

# pour limiter les doublons liés à plusieurs versions du même modèle,
# on garde par défaut la version produite la plus récemment avant la review
filtered = (
    filtered.sort_values(by=["Review Year", "Production Year"], ascending=[True, False])
    .drop_duplicates(subset=["Country", "Make", "Review Year", "Review Score", "Sales Volume"])
)

# on sélectionne et réorganise les colonnes finales
final = filtered[[
    "Country",
    "Make",
    "Car Model",
    "Production Year",
    "Review Year",
    "Review Score",
    "Price",
    "Sales Volume",
    "Engine Type"
]]

# sauvegarde du fichier final
final.to_csv("jointure_resultat.csv", index=False)
print("fichier 'jointure_resultat.csv' créé.")

# connexion à la DB
db_user = 'admin'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'
db_name = 'cars_db'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
final.to_sql("car_reviews", engine, if_exists="replace", index=False)

print("table 'car_reviews' insérée avec succès dans la base.")