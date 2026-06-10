from flask import Blueprint, request, jsonify
from backend.services.sensor_service import save_sensor_data
from database.mongo_service import sensor_collection

api = Blueprint("api", __name__)

CAMPOS_OBRIGATORIOS = [
    "temperatura",
    "umidade_ar",
    "umidade_solo",
    "luminosidade",
    "ndvi"
]


def validar_leitura(data):

    if not isinstance(data, dict):
        return "Corpo da requisição deve ser um JSON"

    for campo in CAMPOS_OBRIGATORIOS:

        if campo not in data:
            return f"Campo obrigatório ausente: {campo}"

        if not isinstance(data[campo], (int, float)) or isinstance(data[campo], bool):
            return f"Campo deve ser numérico: {campo}"

    return None


@api.route("/health", methods=["GET"])
def health():

    return jsonify({"status": "ok"})


@api.route("/sensor-data", methods=["POST"])
def sensor_data():

    data = request.get_json(silent=True)

    erro = validar_leitura(data)

    if erro:
        return jsonify({"error": erro}), 400

    inserted_id = save_sensor_data(data)

    return jsonify({
        "message": "Dados salvos com sucesso",
        "id": inserted_id
    }), 201


@api.route("/latest-data", methods=["GET"])
def latest_data():

    data = sensor_collection.find_one(
        sort=[("timestamp", -1)]
    )

    if not data:
        return jsonify({"message": "Sem dados"}), 404

    data["_id"] = str(data["_id"])

    return jsonify(data)


@api.route("/history", methods=["GET"])
def history():

    data = list(
        sensor_collection
        .find()
        .sort("timestamp", -1)
        .limit(100)
    )

    for item in data:
        item["_id"] = str(item["_id"])

    return jsonify(data)
