from pymongo import MongoClient
import pandas as pd

MONGO_URI = "mongodb+srv://spacefarm:4ge7C79msfKehTYg@spacefarm-cluster.xdsbuuu.mongodb.net/?appName=spacefarm-cluster"

client = MongoClient(MONGO_URI)

db = client["spacefarm"]

collection = db["sensor_readings"]

data = list(collection.find())

for item in data:
    item.pop("_id", None)

df = pd.DataFrame(data)

df.to_csv(
    "ml/datasets/sensor_data.csv",
    index=False
)

print(f"{len(df)} registros exportados")