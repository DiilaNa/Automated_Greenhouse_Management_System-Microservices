import requests
from dotenv import load_dotenv

load_dotenv()

class ConfigLoader:
    _config = {}

    @classmethod
    def load_configs(cls):
        try:
            res = requests.get("http://localhost:8888/automation-service/default")
            data = res.json()
            for source in data.get('propertySources', []):
                cls._config.update(source.get('source', {}))
            print("✅ 8083 Configs Loaded Successfully!")
        except Exception as e:
            print(f"❌ Config Load Error: {e}")

    @classmethod
    def get(cls, key):
        return cls._config.get(key)