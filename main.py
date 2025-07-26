from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()
latest_raw = {"timestamp": None, "raw": ""}

@app.post("/upload_raw")
async def upload_raw(request: Request):
    body = await request.json()
    raw_line = body.get("raw", "")
    latest_raw["timestamp"] = datetime.now().isoformat()
    latest_raw["raw"] = raw_line
    print(f"[RECEIVED] {raw_line}")
    return {"status": "ok"}

@app.get("/latest_raw")
def get_latest_raw():
    return latest_raw