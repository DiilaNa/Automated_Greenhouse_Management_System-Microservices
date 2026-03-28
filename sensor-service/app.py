import py_eureka_client.eureka_client as eureka_client

print("HI")
# Eureka Registration
eureka_client.init(
    eureka_server="http://localhost:8761/eureka",
    app_name="SENSOR-TELEMETRY-SERVICE",
    instance_port=8082,
    instance_host="127.0.0.1"
)