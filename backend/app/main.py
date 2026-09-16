from fastapi import FastAPI
from app.deps import get_settings

app = FastAPI(title="DNA API")

@app.get("/health")
def health():
    return {"status": "ok"}
