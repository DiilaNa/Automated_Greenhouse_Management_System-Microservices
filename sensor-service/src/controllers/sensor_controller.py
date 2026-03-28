from flask import Blueprint, jsonify
from src.models.sensor_model import sensor_store

sensor_bp = Blueprint('sensor', __name__)

@sensor_bp.route('/latest', methods=['GET'])
def get_latest_reading():
    return jsonify(sensor_store.get_data()), 200