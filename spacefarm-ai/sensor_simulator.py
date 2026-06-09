import requests
import random
import time

API_URL = "http://localhost:5000/sensor-data"

while True:

    temperatura = random.randint(22, 38)

    umidade_ar = random.randint(40, 90)

    umidade_solo = max(
        10,
        100 - temperatura + random.randint(-10, 10)
    )

    luminosidade = random.randint(300, 1000)

    ndvi = round(random.uniform(0.2, 0.9), 2)

    payload = {
        "temperatura": temperatura,
        "umidade_ar": umidade_ar,
        "umidade_solo": umidade_solo,
        "luminosidade": luminosidade,
        "ndvi": ndvi
    }

    requests.post(API_URL, json=payload)

    print(payload)

    time.sleep(0.5)