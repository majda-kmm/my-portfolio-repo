from flask import Flask, request, jsonify
from question2.core import generate, statistics, learn, predict
import numpy as np
app = Flask(__name__)

@app.route("/")
def home():
    return "Voilà l'API pour la question 2 :)"

@app.route("/functions")
def functions():
    return jsonify([
        "generate", "statistics", "learn", "predict"
    ])

@app.route("/process")
def process():
    return process_with_problem("classification")

@app.route("/classification/process")
def classification_process():
    return process_with_problem("classification")

@app.route("/regression/process")
def regression_process():
    return process_with_problem("regression")

def process_with_problem(problem):
    n_samples = int(request.args.get("n_samples", 100))
    n_features = int(request.args.get("n_features", 5))

    # génération + apprentissage
    X, y = generate(problem, n_samples, n_features)
    stats = statistics(X, y)
    model, error = learn(problem, X, y)
    preds = predict(model, problem)

    # conversion JSON-safe parce que erreur de type sinon
    stats_clean = {
        "mean_target": float(stats["mean_target"]),
        "std_target": float(stats["std_target"]),
        "mean_features": {k: float(v) for k, v in stats["mean_features"].items()},
        "std_features": {k: float(v) for k, v in stats["std_features"].items()},
        "correlations": {k: np.round(np.array(v), 3).tolist() for k, v in stats["correlations"].items()}
    }

    return jsonify({
        "stats": stats_clean,
        "error": float(error),
        "predictions": [float(p) for p in preds]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)