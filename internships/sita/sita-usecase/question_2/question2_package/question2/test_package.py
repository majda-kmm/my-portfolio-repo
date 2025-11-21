from core import generate, learn, predict, statistics

# teste la génération de données
X, y = generate("classification", 100, 5)

stats = statistics(X, y)
print("Statistiques :", stats)

# entraine un modèle
model, error = learn("classification", X, y)
print("Erreur :", error)

# et predit
preds = predict(model, "classification")
print("Prédictions :", preds)