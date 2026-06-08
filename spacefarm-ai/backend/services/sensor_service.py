from datetime import datetime
from database.mongo_service import sensor_collection


def save_sensor_data(data):

    document = {
        "temperatura": data["temperatura"],
        "umidade_ar": data["umidade_ar"],
        "umidade_solo": data["umidade_solo"],
        "luminosidade": data["luminosidade"],
        "timestamp": datetime.now()
    }

    result = sensor_collection.insert_one(document)

    return str(result.inserted_id)