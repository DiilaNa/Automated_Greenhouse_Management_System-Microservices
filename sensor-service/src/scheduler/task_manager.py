import schedule
import time
import threading
from src.services.telemetry_service import TelemetryService

def job():
    print("Job Function Executed")
    TelemetryService.process_all_telemetry()

def start_scheduler():
    print("Scheduler started")
    schedule.every(10).seconds.do(job)
    
    def run_continuously():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_continuously, daemon=True)
    thread.start()