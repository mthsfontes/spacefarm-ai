import json
import random
from datetime import datetime, timedelta

dados = []

inicio = datetime.now() - timedelta(days=30)

for i in range(10000):

    temperatura = random.randint(20, 40)

    umidade_ar = random.randint(40, 90)

    umidade_solo = max(
        10,
        min(
            100,
            100 - temperatura + random.randint(-10, 15)
        )
    )

    luminosidade = random.randint(300, 1000)

    ndvi = round(random.uniform(0.2, 0.9), 2)

    irrigar = (
        1
        if (
            umidade_solo < 35
            and temperatura > 28
        )
        else 0
    )

    dados.append({
        "temperatura": temperatura,
        "umidade_ar": umidade_ar,
        "umidade_solo": umidade_solo,
        "luminosidade": luminosidade,
        "ndvi": ndvi,
        "irrigar": irrigar,
        "timestamp": (
            inicio + timedelta(minutes=i)
        ).isoformat()
    })

with open(
    "data/sensor_dataset.json",
    "w",
    encoding="utf-8"
) as arquivo:

    json.dump(
        dados,
        arquivo,
        indent=4,
        ensure_ascii=False
    )

print(f"{len(dados)} registros gerados.")