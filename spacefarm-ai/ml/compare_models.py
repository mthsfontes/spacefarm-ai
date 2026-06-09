import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score
)

# Carregar dataset
df = pd.read_csv(
    "ml/datasets/training_data.csv"
)

# Features
X = df[
    [
        "temperatura",
        "umidade_ar",
        "umidade_solo",
        "luminosidade",
        "ndvi"
    ]
]

# Target
y = df["irrigar"]

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------
# Decision Tree
# ------------------------

dt_model = DecisionTreeClassifier()

dt_model.fit(
    X_train,
    y_train
)

dt_predictions = dt_model.predict(
    X_test
)

# ------------------------
# Random Forest
# ------------------------

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(
    X_test
)

# ------------------------
# Métricas
# ------------------------

results = []

results.append({
    "Modelo": "Decision Tree",
    "Accuracy": accuracy_score(
        y_test,
        dt_predictions
    ),
    "Precision": precision_score(
        y_test,
        dt_predictions
    ),
    "Recall": recall_score(
        y_test,
        dt_predictions
    )
})

results.append({
    "Modelo": "Random Forest",
    "Accuracy": accuracy_score(
        y_test,
        rf_predictions
    ),
    "Precision": precision_score(
        y_test,
        rf_predictions
    ),
    "Recall": recall_score(
        y_test,
        rf_predictions
    )
})

results_df = pd.DataFrame(results)

print("\nRESULTADOS:\n")

print(results_df)