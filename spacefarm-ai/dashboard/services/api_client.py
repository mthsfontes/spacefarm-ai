import os

import requests

BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://localhost:5000"
)

TIMEOUT = 5


def get_latest_data():
    response = requests.get(
        f"{BASE_URL}/latest-data",
        timeout=TIMEOUT
    )

    return response.json()


def get_history():
    response = requests.get(
        f"{BASE_URL}/history",
        timeout=TIMEOUT
    )

    return response.json()
