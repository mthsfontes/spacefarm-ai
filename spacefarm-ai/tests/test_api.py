import time

LEITURA_VALIDA = {
    "temperatura": 30,
    "umidade_ar": 60,
    "umidade_solo": 25,
    "luminosidade": 800,
    "ndvi": 0.45
}


def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_salvar_leitura_valida(client, fake_collection):

    response = client.post(
        "/sensor-data",
        json=LEITURA_VALIDA
    )

    assert response.status_code == 201
    assert "id" in response.get_json()
    assert fake_collection.count_documents({}) == 1


def test_leitura_sem_campo_obrigatorio(client):

    leitura = dict(LEITURA_VALIDA)
    leitura.pop("umidade_solo")

    response = client.post(
        "/sensor-data",
        json=leitura
    )

    assert response.status_code == 400
    assert "umidade_solo" in response.get_json()["error"]


def test_leitura_com_campo_nao_numerico(client):

    leitura = dict(LEITURA_VALIDA)
    leitura["temperatura"] = "muito quente"

    response = client.post(
        "/sensor-data",
        json=leitura
    )

    assert response.status_code == 400


def test_leitura_sem_corpo(client):

    response = client.post(
        "/sensor-data",
        data="nao sou json",
        content_type="text/plain"
    )

    assert response.status_code == 400


def test_latest_data_sem_dados(client):

    response = client.get("/latest-data")

    assert response.status_code == 404


def test_latest_data_retorna_mais_recente(client):

    primeira = dict(LEITURA_VALIDA)
    segunda = dict(LEITURA_VALIDA, temperatura=99)

    client.post("/sensor-data", json=primeira)

    # garante timestamps distintos entre as duas leituras
    time.sleep(0.01)

    client.post("/sensor-data", json=segunda)

    response = client.get("/latest-data")

    assert response.status_code == 200
    assert response.get_json()["temperatura"] == 99


def test_history(client):

    for _ in range(3):
        client.post(
            "/sensor-data",
            json=LEITURA_VALIDA
        )

    response = client.get("/history")

    assert response.status_code == 200
    assert len(response.get_json()) == 3
