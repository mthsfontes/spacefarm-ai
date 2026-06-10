from ml.predict_service import predict_irrigation


def test_cenario_seco_recomenda_irrigacao():

    leitura = {
        "temperatura": 38,
        "umidade_ar": 40,
        "umidade_solo": 12,
        "luminosidade": 950,
        "ndvi": 0.25
    }

    prediction, confidence = predict_irrigation(leitura)

    assert prediction == 1
    assert 0 <= confidence <= 1


def test_cenario_umido_nao_recomenda_irrigacao():

    leitura = {
        "temperatura": 22,
        "umidade_ar": 85,
        "umidade_solo": 80,
        "luminosidade": 400,
        "ndvi": 0.85
    }

    prediction, confidence = predict_irrigation(leitura)

    assert prediction == 0
    assert 0 <= confidence <= 1
