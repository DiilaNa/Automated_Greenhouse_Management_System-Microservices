import requests

class ConfigLoader:
    _config = {}

    @classmethod
    def load_from_server(cls):
        try:
            response = requests.get("http://localhost:8888/sensor-telemetry-service/default")
            data = response.json()
            
            for source in data.get('propertySources', []):
                cls._config.update(source.get('source', {}))
            print(f"✅ Configs Keys Loaded: {list(cls._config.keys())}")
            print("✅ Centralized Configs Loaded Successfully!")
        except Exception as e:
            print(f"❌ Error loading from Config Server: {e}")

    @classmethod
    def get(cls, key):
        return cls._config.get(key)