import py_eureka_client.eureka_client as eureka_client
from flask import Flask

from src.config.config_loader import ConfigLoader
from src.controllers.sensor_controller import sensor_bp
from src.scheduler.task_manager import start_scheduler

ConfigLoader.load_from_server()
app = Flask(__name__)

app.register_blueprint(sensor_bp, url_prefix='/api/sensors')

eureka_client.init(
    eureka_server="http://localhost:8761/eureka",
    app_name="SENSOR-TELEMETRY-SERVICE",
    instance_port=8082,
    instance_host="127.0.0.1"
)

if __name__ == '__main__':
    print("inside scheduler")
    start_scheduler()
    print("🚀 Sensor Telemetry Service running on port 8082")
    app.run(host='0.0.0.0', port=8082)