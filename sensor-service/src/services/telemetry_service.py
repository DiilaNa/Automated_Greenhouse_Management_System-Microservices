import requests
from src.models.sensor_model import sensor_store
from src.config.config_loader import ConfigLoader

class TelemetryService:
    @staticmethod
    def process_all_telemetry():
        ZONE_API = ConfigLoader.get('services.zone_url')
        IOT_API_BASE = ConfigLoader.get('external.iot_api_url')
        AUTO_API = ConfigLoader.get('services.automation_url')
        TOKEN = ConfigLoader.get('external.auth_token')

        if not ZONE_API or not IOT_API_BASE:
            print(f"❌ Error: Config missing! ZONE_API: {ZONE_API}, IOT_API_BASE: {IOT_API_BASE}")
            return

        try:
            zones_response = requests.get(ZONE_API, timeout=5)
            if zones_response.status_code != 200:
                print(f"❌ Failed to fetch zones from 8081. Status: {zones_response.status_code}")
                return

            zones = zones_response.json()

            for zone in zones:
                device_id = zone.get('deviceId')
                if not device_id:
                    continue

                fetch_url = f"{IOT_API_BASE}/{device_id}"
                headers = {"Authorization": TOKEN}
                
                res = requests.get(fetch_url, headers=headers, timeout=5)
                
                if res.status_code == 200:
                    telemetry_data = res.json().get('value')
                    print(f"✅ Data fetched for Device: {device_id}")

                    sensor_store.update(telemetry_data)

                    payload = {
                        "zoneId": zone.get('zoneId'),
                        "temperature": telemetry_data.get('temperature'),
                        "humidity": telemetry_data.get('humidity'),
                        "capturedAt": res.json().get('capturedAt')
                    }
                    
                    try:
                        requests.post(AUTO_API, json=payload, timeout=5)
                        print(f"🚀 Pushed to Automation for Zone: {zone.get('zoneId')}")
                    except Exception as e:
                        print(f"⚠️ Automation Service (8083) error: {e}")

        except Exception as e:
            print(f"❌ Critical Error in Telemetry Flow: {e}")