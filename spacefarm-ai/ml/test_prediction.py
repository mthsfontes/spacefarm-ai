from predict_service import (
    predict_irrigation
)

sample = {
    "temperatura": 35,
    "umidade_ar": 40,
    "umidade_solo": 18,
    "luminosidade": 900,
    "ndvi": 0.45
}

prediction, confidence = (
    predict_irrigation(sample)
)

print(prediction)
print(confidence)