import schedule
import time
import threading
from src.services.telemetry_service import TelemetryService

def job():
    print("Running scheduled telemetry task...")
    data = TelemetryService.fetch_from_iot()
    if data:
        TelemetryService.push_to_automation(data)

def start_scheduler():
    schedule.every(10).seconds.do(job)
    
    def run_continuously():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_continuously, daemon=True)
    thread.start()