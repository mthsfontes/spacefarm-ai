from pymongo import MongoClient

MONGO_URI = "mongodb+srv://spacefarm:4ge7C79msfKehTYg@spacefarm-cluster.xdsbuuu.mongodb.net/?appName=spacefarm-cluster"

client = MongoClient(MONGO_URI)

db = client["spacefarm"]

sensor_collection = db["sensor_readings"]