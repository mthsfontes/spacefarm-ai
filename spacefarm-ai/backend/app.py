import logging

from flask import Flask, jsonify
from flask_cors import CORS

from backend.routes import api

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = Flask(__name__)

CORS(app)

app.register_blueprint(api)


@app.errorhandler(404)
def not_found(error):

    return jsonify({"error": "Rota não encontrada"}), 404


@app.errorhandler(500)
def internal_error(error):

    app.logger.exception("Erro interno na API")

    return jsonify({"error": "Erro interno no servidor"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
