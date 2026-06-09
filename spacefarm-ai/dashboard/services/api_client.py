import requests

BASE_URL = "http://localhost:5000"


def get_latest_data():
    response = requests.get(
        f"{BASE_URL}/latest-data"
    )

    return response.json()


def get_history():
    response = requests.get(
        f"{BASE_URL}/history"
    )

    return response.json()