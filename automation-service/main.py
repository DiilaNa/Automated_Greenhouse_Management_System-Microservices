from fastapi import FastAPI, Request
import uvicorn
from src.config.config_loader import ConfigLoader
from src.services.rule_engine import RuleEngine
from py_eureka_client import eureka_client
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    ConfigLoader.load_configs()
    await eureka_client.init_async(
        eureka_server="http://localhost:8761/eureka",
        app_name="AUTOMATION-SERVICE",
        instance_port=8083
    )
    yield

app = FastAPI(title="Automation Service", lifespan=lifespan)

@app.post("/api/automation/process")
async def process_telemetry(request: Request):
    data = await request.json()
    result = RuleEngine.process_data(data)
    return {"message": "Data Processed", "result": result}

@app.get("/api/automation/logs")
async def get_logs():
    return {"logs": "Work in progress..."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)