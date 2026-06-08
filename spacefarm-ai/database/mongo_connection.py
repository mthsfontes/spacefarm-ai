from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "mongodb+srv://spacefarm:4ge7C79msfKehTYg@spacefarm-cluster.xdsbuuu.mongodb.net/?appName=spacefarm-cluster"

client = MongoClient(MONGO_URI)

db = client["spacefarm"]

sensor_collection = db["sensor_readings"]

document = {
    "temperatura": 28,
    "umidade_ar": 65,
    "umidade_solo": 40,
    "luminosidade": 800,
    "timestamp": datetime.now()
}

result = sensor_collection.insert_one(document)

print("ID inserido:", result.inserted_id)