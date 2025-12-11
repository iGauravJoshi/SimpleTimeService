from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root(request: Request):
    # request.client may be None in certain ASGI setups; handle defensively
    client_ip = None
    try:
        if request.client:
            client_ip = request.client.host
    except Exception:
        client_ip = None

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": client_ip or "unknown"
    }
