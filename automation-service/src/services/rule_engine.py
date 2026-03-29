import requests
from src.config.config_loader import ConfigLoader

class RuleEngine:
    @staticmethod
    def process_data(payload):
        zone_id = payload.get('zoneId')
        current_temp = payload.get('temperature')

        base_url = ConfigLoader.get('services.zone_url')
        if not base_url:
            print("❌ Error: services.zone_url is missing in Configs!")
            return None

        ZONE_SERVICE_URL = f"{base_url}/{zone_id}"

        try:
            res = requests.get(ZONE_SERVICE_URL, timeout=5)
            if res.status_code == 200:
                zone_details = res.json()
                max_temp = zone_details.get('maxTemp')
                min_temp = zone_details.get('minTemp')

                action = "STABLE"
                if current_temp > max_temp:
                    action = "TURN_FAN_ON"
                elif current_temp < min_temp:
                    action = "TURN_HEATER_ON"

                print(f"🤖 [Rule Engine] Zone: {zone_id} | Temp: {current_temp} | Action: {action}")
                
                return {
                    "zoneId": zone_id,
                    "status": action,
                    "thresholds": {"min": min_temp, "max": max_temp}
                }
        except Exception as e:
            print(f"❌ Error in Rule Engine: {e}")
        return None