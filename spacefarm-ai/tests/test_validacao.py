from backend.routes import validar_leitura

LEITURA_VALIDA = {
    "temperatura": 30,
    "umidade_ar": 60,
    "umidade_solo": 25,
    "luminosidade": 800,
    "ndvi": 0.45
}


def test_leitura_valida():

    assert validar_leitura(LEITURA_VALIDA) is None


def test_corpo_nao_dict():

    assert validar_leitura(None) is not None
    assert validar_leitura([1, 2]) is not None


def test_campo_ausente():

    leitura = dict(LEITURA_VALIDA)
    leitura.pop("ndvi")

    erro = validar_leitura(leitura)

    assert erro is not None
    assert "ndvi" in erro


def test_campo_booleano_rejeitado():

    leitura = dict(LEITURA_VALIDA, temperatura=True)

    assert validar_leitura(leitura) is not None
