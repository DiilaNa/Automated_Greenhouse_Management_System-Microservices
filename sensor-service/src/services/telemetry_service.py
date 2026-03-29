import requests
import os
import random # Mock data වෙනස් වෙන්න මේක ගමු
from src.models.sensor_model import sensor_store
from src.config.config_loader import ConfigLoader
from dotenv import load_dotenv

load_dotenv()

class TelemetryService:
    _current_token = None

    # --- කලින් තිබුණ Real Logic එක (මුකුත් වෙනස් කළේ නැහැ) ---
    @staticmethod
    def get_new_access_token():
        print("🔄 Attempting to refresh Access Token...")
        REFRESH_URL = "http://104.211.95.241:8080/api/auth/refresh"
        refresh_token = os.getenv('EXTERNAL_REFRESH_TOKEN') or ConfigLoader.get('external.refresh_token')

        if not refresh_token:
            print("❌ Error: No Refresh Token found in .env or Config Server!")
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
                print(f"❌ Refresh failed: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Refresh API Error: {e}")
            return None

    # @staticmethod
    # def process_all_telemetry():
    #
    #     print("\n--- ⏳ Telemetry Cycle (REAL MODE) Started ---")
    #     ZONE_API = ConfigLoader.get('services.zone_url')
    #     IOT_API_BASE = ConfigLoader.get('external.iot_api_url')
    #     AUTO_API = ConfigLoader.get('services.automation_url')
    #
    #     if not ZONE_API: return
    #     if not TelemetryService._current_token: TelemetryService.get_new_access_token()
    #
    #     try:
    #         res = requests.get(ZONE_API, timeout=10)
    #         if res.status_code == 200:
    #             zones = res.json()
    #             for zone in zones:
    #                 device_id = zone.get('deviceId')
    #                 if not device_id or device_id == "dev-001": continue
    #
    #                 fetch_url = f"{IOT_API_BASE}/{device_id}"
    #                 headers = {"Authorization": TelemetryService._current_token}
    #                 response = requests.get(fetch_url, headers=headers, timeout=5)
    #
    #                 if response.status_code == 200:
    #                     data = response.json().get('value')
    #
    #                     print(f"🌡️ Real Data for {zone.get('zoneId')}: {data.get('temperature')}°C")
    #
    #                     requests.post(AUTO_API, json={"zoneId": zone.get('zoneId'), "temperature": data.get('temperature'), "humidity": data.get('humidity')}, timeout=2)
    #     except Exception as e:
    #         print(f"❌ Error: {e}")

    @staticmethod
    def process_all_telemetry():
        print("\n--- 🧪 Telemetry Cycle (MOCK MODE) Started ---")
        AUTO_API = ConfigLoader.get('services.automation_url')


        mock_temp = round(random.uniform(25.0, 40.0), 2)
        mock_zone = "ZONE-004"

        print(f"🌡️ Generated Mock Temp: {mock_temp}°C for {mock_zone}")

        payload = {
            "zoneId": mock_zone,
            "temperature": mock_temp,
            "humidity": 55.5,
            "capturedAt": "2026-03-29T14:00:00Z"
        }

        try:
            requests.post(AUTO_API, json=payload, timeout=2)
            print(f"🚀 Pushed MOCK data to Automation (8083)")
        except:
            print(f"⚠️ 8083 (Automation Service) is unreachable.")