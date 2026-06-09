import joblib
import pandas as pd

model = joblib.load(
    "ml/models/irrigation_model.pkl"
)

def predict_irrigation(data):

    sample = pd.DataFrame([
        {
            "temperatura": data["temperatura"],
            "umidade_ar": data["umidade_ar"],
            "umidade_solo": data["umidade_solo"],
            "luminosidade": data["luminosidade"],
            "ndvi": data["ndvi"]
        }
    ])

    prediction = model.predict(sample)[0]

    confidence = max(
        model.predict_proba(sample)[0]
    )

    return prediction, confidence