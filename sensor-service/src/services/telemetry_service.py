import requests
import os
from src.models.sensor_model import sensor_store

class TelemetryService:
    @staticmethod
    def fetch_from_iot():
        IOT_API_URL = "http://external-iot-api.com/api/sensors" 
        TOKEN = "Bearer your_token_here"
        
        try:
            response = requests.get(IOT_API_URL, headers={"Authorization": TOKEN}, timeout=5)
            if response.status_code == 200:
                data = response.json()
                sensor_store.update(data)
                return data
        except Exception as e:
            print(f"Error fetching: {e}")
        return None

    @staticmethod
    def push_to_automation(data):
        PUSH_URL = "http://localhost:8083/api/automation/process"
        try:
            requests.post(PUSH_URL, json=data, timeout=5)
            print("Successfully pushed to Automation Service")
        except Exception as e:
            print(f"Error pushing: {e}")