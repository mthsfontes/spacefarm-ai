from flask import Blueprint, request, jsonify
from backend.services.sensor_service import save_sensor_data
from database.mongo_service import sensor_collection

api = Blueprint("api", __name__)

@api.route("/sensor-data", methods=["POST"])
def sensor_data():

    data = request.get_json()

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