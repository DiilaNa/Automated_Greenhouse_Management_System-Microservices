import requests
from src.models.sensor_model import sensor_store
from src.config.config_loader import ConfigLoader

class TelemetryService:
    _current_token = None

    @staticmethod
    def get_new_access_token():
        print("🔄 Attempting to refresh Access Token...")
        REFRESH_URL = "http://104.211.95.241:8080/api/auth/refresh"
        refresh_token = ConfigLoader.get('external.refresh_token')

        if not refresh_token:
            print("❌ Error: No Refresh Token found in Config Server!")
            return None

        try:
            payload = {"refreshToken": refresh_token}
            response = requests.post(REFRESH_URL, json=payload, timeout=5)

            if response.status_code == 200:
                new_token = response.json().get('accessToken')
                TelemetryService._current_token = f"Bearer {new_token}"
                print("✅ Token refreshed successfully!")
                return TelemetryService._current_token
            else:
                print(f"❌ Refresh failed: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"❌ Refresh API Error: {e}")
            return None

    @staticmethod
    def process_all_telemetry():
        print("\n--- ⏳ Telemetry Cycle Started ---")
        ZONE_API = ConfigLoader.get('services.zone_url')
        IOT_API_BASE = ConfigLoader.get('external.iot_api_url')
        AUTO_API = ConfigLoader.get('services.automation_url')

        if not TelemetryService._current_token:
            TelemetryService.get_new_access_token()

        try:
            res = requests.get(ZONE_API, timeout=5)
            if res.status_code != 200:
                print(f"❌ Failed to fetch zones: {res.status_code}")
                return

            zones = res.json()
            for zone in zones:
                device_id = zone.get('deviceId')
                if not device_id or device_id == "dev-001": continue

                fetch_url = f"{IOT_API_BASE}/{device_id}"

                headers = {"Authorization": TelemetryService._current_token}
                response = requests.get(fetch_url, headers=headers, timeout=5)

                if response.status_code == 401:
                    print(f"⚠️ 401 Unauthorized for {device_id}. Refreshing token...")
                    if TelemetryService.get_new_access_token():
                        # අලුත් ටෝකන් එකෙන් ආයෙත් කෝල් කරනවා
                        headers = {"Authorization": TelemetryService._current_token}
                        response = requests.get(fetch_url, headers=headers, timeout=5)

                if response.status_code == 200:
                    data = response.json().get('value')
                    print(f"🌡️ Data for {zone.get('zoneId')}: {data.get('temperature')}°C")

                    sensor_store.update(data)

                    payload = {
                        "zoneId": zone.get('zoneId'),
                        "temperature": data.get('temperature'),
                        "humidity": data.get('humidity'),
                        "capturedAt": response.json().get('capturedAt')
                    }
                    requests.post(AUTO_API, json=payload, timeout=2)
                    print(f"🚀 Pushed to Automation for {zone.get('zoneId')}")
                else:
                    print(f"❌ Failed to fetch for {device_id}: Status {response.status_code}")

        except Exception as e:
            print(f"❌ Telemetry Flow Error: {e}")