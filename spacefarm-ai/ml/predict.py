import joblib
import pandas as pd

model = joblib.load(
    "ml/models/irrigation_model.pkl"
)

sample = pd.DataFrame([
    {
        "temperatura": 35,
        "umidade_ar": 50,
        "umidade_solo": 20,
        "luminosidade": 900,
        "ndvi": 0.40
    }
])

prediction = model.predict(sample)

if prediction[0] == 1:
    print("IRRIGAR")
else:
    print("NAO IRRIGAR")