"""Script de teste de conexão com o MongoDB.

Insere um documento de exemplo na coleção para validar
que a conexão configurada no .env está funcionando.
"""

import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

from database.mongo_service import sensor_collection

document = {
    "temperatura": 28,
    "umidade_ar": 65,
    "umidade_solo": 40,
    "luminosidade": 800,
    "ndvi": 0.7,
    "timestamp": datetime.now()
}

result = sensor_collection.insert_one(document)

print("ID inserido:", result.inserted_id)
