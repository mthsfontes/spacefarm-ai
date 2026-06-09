import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# Variável alvo
y = df["irrigar"]

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Treinar modelo
model = DecisionTreeClassifier()

model.fit(
    X_train,
    y_train
)

# Fazer previsões
predictions = model.predict(
    X_test
)

# Calcular acurácia
accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"Accuracy: {accuracy:.2f}"
)

# Salvar modelo
joblib.dump(
    model,
    "ml/models/irrigation_model.pkl"
)

print("Modelo salvo com sucesso!")