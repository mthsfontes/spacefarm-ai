import logging
import os
import random
import time

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("sensor_simulator")

API_URL = os.getenv(
    "API_URL",
    "http://localhost:5000/sensor-data"
)

INTERVALO_SEGUNDOS = float(
    os.getenv("INTERVALO_SEGUNDOS", "0.5")
)


def gerar_leitura():

    temperatura = random.randint(22, 38)

    umidade_ar = random.randint(40, 90)

    umidade_solo = max(
        10,
        100 - temperatura + random.randint(-10, 10)
    )

    luminosidade = random.randint(300, 1000)

    ndvi = round(random.uniform(0.2, 0.9), 2)

    return {
        "temperatura": temperatura,
        "umidade_ar": umidade_ar,
        "umidade_solo": umidade_solo,
        "luminosidade": luminosidade,
        "ndvi": ndvi
    }


if __name__ == "__main__":

    logger.info("Simulador iniciado, enviando para %s", API_URL)

    while True:

        payload = gerar_leitura()

        try:
            response = requests.post(
                API_URL,
                json=payload,
                timeout=5
            )

            response.raise_for_status()

            logger.info("Leitura enviada: %s", payload)

        except requests.exceptions.RequestException as erro:
            logger.warning(
                "Falha ao enviar leitura (%s). Nova tentativa em instantes.",
                erro
            )

        time.sleep(INTERVALO_SEGUNDOS)
