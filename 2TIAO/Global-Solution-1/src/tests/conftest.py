import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

# URI falsa para os testes não dependerem do banco real
os.environ.setdefault(
    "MONGO_URI",
    "mongodb://localhost:27017/"
)

import mongomock
import pytest


@pytest.fixture
def fake_collection(monkeypatch):
    """Substitui a coleção real do Mongo por uma em memória."""

    collection = (
        mongomock.MongoClient()
        ["spacefarm"]
        ["sensor_readings"]
    )

    import backend.routes as routes
    import backend.services.sensor_service as sensor_service

    monkeypatch.setattr(
        routes,
        "sensor_collection",
        collection
    )

    monkeypatch.setattr(
        sensor_service,
        "sensor_collection",
        collection
    )

    return collection


@pytest.fixture
def client(fake_collection):
    """Cliente de teste da API Flask."""

    from backend.app import app

    app.config["TESTING"] = True

    return app.test_client()
