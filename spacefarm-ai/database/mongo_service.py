import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError(
        "Variável MONGO_URI não definida. "
        "Crie um arquivo .env baseado no .env.example."
    )

client = MongoClient(MONGO_URI)

db = client["spacefarm"]

sensor_collection = db["sensor_readings"]
