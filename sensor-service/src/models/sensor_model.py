class SensorData:
    def __init__(self):
        self.latest_reading = {
            "temperature": 0.0,
            "humidity": 0.0,
            "status": "No data fetched yet"
        }

    def update(self, data):
        self.latest_reading = data

    def get_data(self):
        return self.latest_reading

# Singleton instance
sensor_store = SensorData()